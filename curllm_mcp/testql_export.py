"""Export curllm execution results to TestQL scenarios."""

from __future__ import annotations

import os
import platform
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    from testql.export.scenario_builder import ScenarioBuilder
except ImportError:
    ScenarioBuilder = None  # type: ignore[misc, assignment]


def testql_export_enabled() -> bool:
    return os.getenv("CURLLM_EMIT_TESTQL", "0").strip().lower() in {
        "1", "true", "yes", "on",
    }


def _csv(value: Any) -> str:
    text = str(value if value is not None else "-").strip()
    return text.replace(",", ";") or "-"


def _detect_environment(*, captcha: bool = False) -> dict[str, str]:
    session = os.environ.get("XDG_SESSION_TYPE", "").strip().lower()
    display = "wayland" if session == "wayland" or os.environ.get("WAYLAND_DISPLAY") else "x11"
    return {
        "os": platform.system().lower(),
        "session": session or display,
        "display": display,
        "browser.engine": "chromium",
        "browser.headless": "false" if os.environ.get("CURLLM_VISUAL", "0") == "1" else "true",
        "app.type": "web",
        "runtime.source": "curllm",
        "runtime.captcha_solver": "true" if captcha else "false",
    }


def build_testql_scenario_text(
    *,
    instruction: str,
    url: str | None,
    result: dict[str, Any],
    captcha_solver: bool = False,
    visual_mode: bool = False,
) -> str:
    """Build TestTOON scenario for curllm workflow replay."""
    target = url or _extract_url_from_instruction(instruction) or "https://example.com"
    parsed = urlparse(target)
    base_url = f"{parsed.scheme}://{parsed.netloc}" if parsed.netloc else target
    success = result.get("success", result.get("ok", False))
    steps_taken = result.get("steps_taken", result.get("steps", 0))

    env = _detect_environment(captcha=captcha_solver)
    if visual_mode:
        env["browser.headless"] = "false"

    suggested = result.get("suggested_commands") or []
    flow_rows = [
        {"command": "LOG", "target": "instruction", "value": instruction},
        {"command": "LOG", "target": "steps_taken", "value": str(steps_taken)},
    ]
    for idx, cmd in enumerate(suggested[:10]):
        flow_rows.append({"command": "LOG", "target": f"suggested_{idx}", "value": _csv(cmd)})

    if ScenarioBuilder is not None:
        builder = (
            ScenarioBuilder(
                name="curllm-replay-from-execution",
                scenario_type="gui",
                meta={"SOURCE": "curllm.execution.v1"},
            )
            .environment(env)
            .config({
                "target_url": base_url,
                "browser.base_url": base_url,
                "curllm_instruction": _csv(instruction),
                "execution_success": "true" if success else "false",
                "steps_taken": str(steps_taken),
                "run_log": _csv(result.get("run_log")),
            })
            .context({
                "instruction": instruction,
                "url": target,
                "captcha_solver": str(captcha_solver).lower(),
                "visual_mode": str(visual_mode).lower(),
            })
            .commands([
                "CONTEXT_DETECT source=curllm",
                f"GUI_START ${'{'}target_url{'}'}",
            ])
            .flow(flow_rows)
            .shell([
                f"curllm-mcp --help >/dev/null 2>&1 || python -c \"import curllm_mcp\"",
            ])
            .commands(["GUI_STOP"])
        )
        return builder.build()

    return f"""# SCENARIO: curllm-replay-from-execution
# TYPE: gui
# SOURCE: curllm.execution.v1

CONFIG[3]{{key, value}}:
  target_url,  {base_url}
  curllm_instruction,  {_csv(instruction)}
  execution_success,  {'true' if success else 'false'}

COMMANDS[2]{{command}}:
  GUI_START ${{target_url}}
  GUI_STOP
"""


def _extract_url_from_instruction(text: str) -> str | None:
    import re

    match = re.search(r"https?://[^\s<>\"']+", text, re.I)
    return match.group(0).rstrip(".,);]") if match else None


def maybe_write_testql_scenario(
    *,
    instruction: str,
    url: str | None,
    result: dict[str, Any],
    output_dir: str | Path | None = None,
    captcha_solver: bool = False,
    visual_mode: bool = False,
) -> Path | None:
    if not testql_export_enabled():
        return None
    out = Path(output_dir or os.getenv("CURLLM_TESTQL_DIR", "recordings"))
    out.mkdir(parents=True, exist_ok=True)
    from datetime import datetime, timezone

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = out / f"curllm_{stamp}.testql.toon.yaml"
    path.write_text(
        build_testql_scenario_text(
            instruction=instruction,
            url=url,
            result=result,
            captcha_solver=captcha_solver,
            visual_mode=visual_mode,
        ),
        encoding="utf-8",
    )
    return path
