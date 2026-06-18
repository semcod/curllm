import os
from pathlib import Path
from dataclasses import dataclass, field


def default_log_dir() -> str:
    """
    Resolve log directory anchored to current working directory.
    - If CURLLM_LOG_DIR is set:
        * absolute path is used as-is
        * relative path is resolved against cwd
    - Otherwise defaults to <cwd>/logs
    """
    env_dir = os.getenv("CURLLM_LOG_DIR")

    if env_dir:
        path = Path(env_dir).expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        return str(path)

    return str(Path.cwd() / "logs")


def default_screenshot_dir() -> str:
    """
    Resolve screenshot directory anchored to current working directory.
    - If CURLLM_SCREENSHOT_DIR is set:
        * absolute path is used as-is
        * relative path is resolved against cwd
    - Otherwise defaults to <cwd>/screenshots
    """
    env_dir = os.getenv("CURLLM_SCREENSHOT_DIR")

    if env_dir:
        path = Path(env_dir).expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        return str(path)

    return str(Path.cwd() / "screenshots")


@dataclass
class OrchestratorConfig:
    """Configuration for orchestrator"""
    headless: bool = True
    stealth_mode: bool = True
    timeout_seconds: int = 120
    screenshot_on_error: bool = True
    screenshot_on_success: bool = True
    screenshot_each_step: bool = False  # Capture after each step
    log_to_file: bool = True
    log_dir: str = field(default_factory=default_log_dir)  # Resolved at runtime
    screenshot_dir: str = field(default_factory=default_screenshot_dir)  # Resolved at runtime
    dry_run: bool = False  # Parse and plan only, don't execute
    auto_captcha_visible: bool = True  # Auto-switch to visible mode on CAPTCHA
    captcha_wait_seconds: int = 60  # How long to wait for user to solve CAPTCHA

