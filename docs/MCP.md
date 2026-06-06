# curllm MCP — narzędzia dla agentów LLM

curllm udostępnia te same operacje przez **CLI**, **REST** (`curllm-web`) i **MCP** (`curllm-mcp`).

## Instalacja

Z katalogu głównego repozytorium:

```bash
cd ~/github/wronai/curllm
pip install -e ".[mcp]"
```

## Uruchomienie

```bash
curllm-mcp
# lub: python -m curllm_mcp.server
```

## Narzędzia MCP

| Tool | Opis |
|------|------|
| `curllm_interfaces` | Powierzchnie integracji (CLI, REST, MCP) |
| `curllm_health` | Ollama + curllm API |
| `curllm_list_models` | Modele Ollama |
| `curllm_fetch_light` | Szybki HTTP fetch (tytuł, streszczenie, linki) bez Playwright |
| `curllm_execute` | Pełny workflow Playwright + lokalny LLM |
| `curllm_extract` | Ekstrakcja danych ze strony |
| `curllm_fill_form` | Wypełnianie formularza z języka naturalnego |

## Konfiguracja Cursor / Claude Desktop

```json
{
  "mcpServers": {
    "curllm": {
      "command": "curllm-mcp",
      "cwd": "/home/tom/github/wronai/curllm",
      "env": {
        "CURLLM_API_HOST": "http://localhost:8810",
        "OLLAMA_HOST": "http://localhost:11434"
      }
    }
  }
}
```

## Tryby wykonania

- **Domyślnie** (`curllm_execute`): in-process `CurllmExecutor` (Playwright + Ollama).
- **Przez REST** (`use_api=true` lub `CURLLM_MCP_USE_API=1`): proxy do `POST /api/execute`.
- **Lekki fetch** (`curllm_fetch_light`): tylko HTTP — bez LLM i przeglądarki.

## REST (alternatywa)

```bash
curl -sS -X POST "$CURLLM_API_HOST/api/execute" \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","data":"extract all links"}' | jq .
```

Pełna dokumentacja REST: [docs/v2/api/API.md](v2/api/API.md).
