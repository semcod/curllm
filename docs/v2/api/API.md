# API

**[📚 Documentation Index](INDEX.md)** | **[⬅️ Back to Main README](../README.md)**

---

## Surfaces

| Surface | Entry | Use case |
|---------|-------|----------|
| **CLI** | `curllm` | Shell, scripts |
| **REST** | `curllm-web` → `http://localhost:8810` | HTTP clients, Todomat adapter |
| **MCP** | `curllm-mcp` | LLM agents (Cursor, Claude Desktop) |

Discover surfaces at runtime:

```bash
curl http://localhost:8810/api/interfaces
```

MCP docs: [docs/MCP.md](../../MCP.md)

## REST Endpoints

- GET `/health`
  - Returns server status and model info.

- GET `/api/interfaces`
  - Lists CLI, REST, and MCP surfaces with available tools and endpoints.

- POST `/api/execute`
  - Content-Type: application/json
  - Payload:
    ```json
    {
      "url": "https://example.com",
      "data": "instruction or query",
      "visual_mode": false,
      "stealth_mode": false,
      "captcha_solver": false,
      "use_bql": false,
      "headers": {"Accept-Language": "pl-PL,pl;q=0.9"}
    }
    ```
  - Response shape:
    ```json
    {
      "success": true,
      "result": {"...": "..."},
      "screenshots": ["screenshots/domain/step_0_xxx.png"],
      "steps_taken": 3,
      "run_log": "logs/run-YYYYMMDD-HHMMSS.md",
      "timestamp": "2025-11-24T08:27:36.528Z"
    }
    ```

- GET `/api/models`
  - Lists available Ollama models.

- GET `/api/screenshot/<filename>`
  - Serves saved screenshots.

## Headers

- Set `Accept-Language` to influence content language (examples send this automatically if `ACCEPT_LANGUAGE` is defined).

## Example requests

- curl (raw):
  ```bash
  curl -sS -X POST "$CURLLM_API_HOST/api/execute" \
    -H 'Content-Type: application/json' \
    -d '{"url":"https://example.com","data":"extract all links"}' | jq .
  ```

- Node.js: see `examples/node_api_example.js`
- PHP: see `examples/php_api_example.php`
