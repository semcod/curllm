#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v curllm-mcp >/dev/null 2>&1; then
  pip install -e ".[mcp]" -q
fi

export CURLLM_API_HOST="${CURLLM_API_HOST:-http://localhost:8810}"
export OLLAMA_HOST="${OLLAMA_HOST:-http://localhost:11434}"

exec curllm-mcp
