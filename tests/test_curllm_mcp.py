"""Tests for curllm_mcp service layer (no Playwright)."""

from curllm_mcp.service import CurllmService


def test_interfaces_info():
    info = CurllmService().interfaces_info()
    assert info["name"] == "curllm"
    assert "curllm-mcp" in info["mcp_entrypoint"]
    assert "curllm_execute" in info["mcp_tools"]


def test_fetch_light_example_com():
    svc = CurllmService()
    result = svc.fetch_light("check https://example.com")
    assert result["success"] is True
    assert result["url"] == "https://example.com"
    assert "Example" in (result.get("title") or result.get("summary") or "")


def test_fetch_light_missing_url():
    result = CurllmService().fetch_light("no url here")
    assert result["success"] is False
    assert "URL" in result["error"]


def test_extract_url_helper():
    assert CurllmService._extract_url("visit https://foo.bar/page", None) == "https://foo.bar/page"
    assert CurllmService._extract_url("text", "https://x.test") == "https://x.test"
