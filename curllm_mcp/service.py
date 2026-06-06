"""Shared service layer for REST, SDK, and MCP."""

from __future__ import annotations

import asyncio
import json
import os
import re
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urlparse

import requests

from curllm_core.config import config

URL_RE = re.compile(r"https?://[^\s<>\"']+", re.I)


class _TitleLinksParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self._in_title = True
        if tag == "a":
            href = dict(attrs).get("href") or ""
            if href.startswith("http"):
                self.links.append({"href": href, "text": ""})

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


class CurllmService:
    """Facade for curllm automation — used by MCP tools and HTTP clients."""

    def __init__(self, api_host: str | None = None) -> None:
        self.api_host = (
            api_host
            or os.getenv("CURLLM_API_HOST")
            or f"http://localhost:{config.api_port}"
        ).rstrip("/")

    def interfaces_info(self) -> dict[str, Any]:
        return {
            "name": "curllm",
            "version": "1.0.40",
            "surfaces": ["cli", "rest", "mcp"],
            "mcp_entrypoint": "curllm-mcp",
            "rest_endpoints": [
                "GET /health",
                "POST /api/execute",
                "GET /api/models",
                "GET /api/proxy/list",
                "POST /api/proxy/register",
                "POST /api/proxy/health",
            ],
            "mcp_tools": [
                "curllm_interfaces",
                "curllm_health",
                "curllm_list_models",
                "curllm_fetch_light",
                "curllm_execute",
                "curllm_extract",
                "curllm_fill_form",
            ],
            "default_api_host": self.api_host,
            "ollama_host": config.ollama_host,
            "model": config.ollama_model,
        }

    def health(self) -> dict[str, Any]:
        ollama_ok = False
        ollama_error: str | None = None
        try:
            r = requests.get(f"{config.ollama_host}/api/tags", timeout=3)
            ollama_ok = r.status_code == 200
        except Exception as exc:
            ollama_error = str(exc)

        api_ok = False
        api_error: str | None = None
        try:
            r = requests.get(f"{self.api_host}/health", timeout=3)
            api_ok = r.status_code == 200
        except Exception as exc:
            api_error = str(exc)

        return {
            "status": "ok" if ollama_ok or api_ok else "degraded",
            "ollama_host": config.ollama_host,
            "ollama_reachable": ollama_ok,
            "ollama_error": ollama_error,
            "api_host": self.api_host,
            "api_reachable": api_ok,
            "api_error": api_error,
            "model": config.ollama_model,
        }

    def list_models(self) -> dict[str, Any]:
        try:
            r = requests.get(f"{config.ollama_host}/api/tags", timeout=10)
            r.raise_for_status()
            return {"success": True, "models": r.json()}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    @staticmethod
    def _extract_url(text: str, url: str | None = None) -> str | None:
        if url:
            return url.strip()
        match = URL_RE.search(text)
        return match.group(0).rstrip(".,);]") if match else None

    def fetch_light(self, text: str, url: str | None = None) -> dict[str, Any]:
        target = self._extract_url(text, url)
        if not target:
            return {"success": False, "error": "Brak URL — podaj url lub https://... w tekście"}

        try:
            r = requests.get(
                target,
                timeout=30,
                headers={"User-Agent": "curllm-mcp/1.0", "Accept-Language": config.locale},
            )
            r.raise_for_status()
            parser = _TitleLinksParser()
            parser.feed(r.text[:500_000])
            paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", r.text[:100_000], re.I | re.S)
            summary = " ".join(
                re.sub(r"<[^>]+>", " ", p).strip() for p in paragraphs[:6] if p.strip()
            )[:2000]

            return {
                "success": True,
                "mode": "light_http",
                "url": target,
                "title": parser.title.strip(),
                "summary": summary or parser.title.strip(),
                "links": parser.links[:30],
                "status_code": r.status_code,
            }
        except Exception as exc:
            return {"success": False, "url": target, "error": str(exc)}

    def _execute_via_api(self, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            r = requests.post(f"{self.api_host}/api/execute", json=payload, timeout=config.llm_timeout)
            if r.status_code >= 400:
                return {"success": False, "error": r.text, "status_code": r.status_code}
            data = r.json()
            if isinstance(data, dict):
                return data
            return {"success": True, "result": data}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    def _execute_in_process(self, payload: dict[str, Any]) -> dict[str, Any]:
        from curllm_core.execution.executor import CurllmExecutor

        executor = CurllmExecutor()

        def _run() -> dict[str, Any]:
            loop = asyncio.new_event_loop()
            try:
                asyncio.set_event_loop(loop)
                return loop.run_until_complete(
                    executor.execute_workflow(
                        instruction=payload.get("data") or payload.get("instruction") or "",
                        url=payload.get("url"),
                        visual_mode=bool(payload.get("visual_mode")),
                        stealth_mode=bool(payload.get("stealth_mode")),
                        captcha_solver=bool(payload.get("captcha_solver")),
                        use_bql=bool(payload.get("use_bql")),
                        headers=payload.get("headers") or {},
                        proxy=payload.get("proxy"),
                        session_id=payload.get("session_id"),
                        wordpress_config=payload.get("wordpress_config"),
                        use_v2=not bool(payload.get("use_v1")),
                    )
                )
            finally:
                loop.close()

        try:
            result = _run()
            if isinstance(result, dict):
                return result
            return {"success": True, "result": result}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    def execute(
        self,
        instruction: str,
        url: str | None = None,
        *,
        visual_mode: bool = False,
        stealth_mode: bool = False,
        captcha_solver: bool = False,
        use_bql: bool = False,
        use_api: bool | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        target_url = self._extract_url(instruction, url)
        payload = {
            "url": target_url,
            "data": instruction,
            "visual_mode": visual_mode,
            "stealth_mode": stealth_mode,
            "captcha_solver": captcha_solver,
            "use_bql": use_bql,
            "headers": headers or {"Accept-Language": f"{config.locale},{config.locale.split('-')[0]};q=0.9"},
        }

        prefer_api = use_api if use_api is not None else os.getenv("CURLLM_MCP_USE_API", "0") == "1"
        if prefer_api:
            return self._execute_via_api(payload)
        return self._execute_in_process(payload)

    def extract(self, url: str, instruction: str, **kwargs: Any) -> dict[str, Any]:
        prompt = instruction.strip() or "extract page title, summary and all links"
        if url not in prompt:
            prompt = f"{prompt} — {url}"
        return self.execute(prompt, url=url, **kwargs)

    def fill_form(self, url: str, instruction: str, **kwargs: Any) -> dict[str, Any]:
        prompt = instruction.strip() or "fill and submit the contact form"
        if url not in prompt:
            prompt = f"On {url}: {prompt}"
        return self.execute(prompt, url=url, **kwargs)
