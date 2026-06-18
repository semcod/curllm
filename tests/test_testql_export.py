"""Tests for curllm → TestQL export."""

from __future__ import annotations

from curllm_mcp.testql_export import build_testql_scenario_text, testql_export_enabled


def test_build_testql_scenario_text_contains_environment() -> None:
    text = build_testql_scenario_text(
        instruction="zaloguj na blog https://example.com/wp-login.php",
        url="https://example.com/wp-login.php",
        result={"success": True, "steps_taken": 3, "suggested_commands": ["click #login"]},
        captcha_solver=True,
    )
    assert "ENVIRONMENT[" in text
    assert "runtime.source" in text
    assert "curllm" in text
    assert "GUI_START" in text
    assert "captcha_solver" in text


def test_testql_export_disabled_by_default(monkeypatch) -> None:
    monkeypatch.delenv("CURLLM_EMIT_TESTQL", raising=False)
    assert testql_export_enabled() is False
