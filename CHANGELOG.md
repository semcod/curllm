# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.40] - 2026-02-24

### Changed
- Refactored core logic into `curllm_core` package
- Slimmed down `curllm_server.py` to thin shim
- Moved `bql_parser.py` into `curllm_core/bql.py`

### Fixed
- pyproject.toml: removed duplicate `license` field

## [1.0.0] - 2025-01-01

### Added
- Initial release of curllm
- Browser automation with local LLMs (Ollama)
- BQL (Browser Query Language) DSL
- Playwright integration for web scraping
- CAPTCHA detection support
- Visual scraping mode
- URL monitoring with cron support
