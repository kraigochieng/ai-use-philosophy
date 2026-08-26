# ai-use-philosophy

An [MCP](https://modelcontextprotocol.io) server that stores your personal
**AI-use philosophy** — a running list of principles for how you want AI
assistants to behave — and serves them to any MCP client so they can be loaded
and applied to a conversation on demand.

## How it works

Principles are plain text rows in a database. The server exposes them through:

| Kind   | Name                   | Description                                             |
| ------ | ---------------------- | ------------------------------------------------------ |
| Prompt | `apply_all_principles` | Returns every stored principle wrapped in an instruction to apply them to the conversation. |
| Tool   | `add_principle`        | Add a new principle.                                    |
| Tool   | `list_principles`      | List all principles with their ids.                    |
| Tool   | `edit_principle`       | Replace the text of a principle by id.                 |
| Tool   | `delete_principle`     | Delete a principle by id.                              |

The server runs over the **streamable-HTTP** transport and listens at `/mcp`.
Visiting the site root (`/`) serves a plain-text page with setup directions.

A hosted instance is available at **https://ai-use-philosophy.onrender.com/mcp**.

## Requirements

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
cp .env.example .env   # adjust if needed
uv run ai-use-philosophy
```

The server starts on `http://0.0.0.0:8000/mcp` by default.

## Configuration

Settings are read from the environment (or a `.env` file):

| Variable | Default                     | Description                              |
| -------- | --------------------------- | --------------------------------------- |
| `PORT`   | `8000`                      | Port to listen on.                       |
| `HOST`   | `0.0.0.0`                   | Address to bind to.                      |
| `DB_URL` | `sqlite:///principles.db`   | SQLAlchemy database URL.                 |

## Database

By default principles are stored in a local SQLite file (`principles.db`), and
the `principles` table is created automatically on startup.

To use PostgreSQL, set `DB_URL`, e.g.:

```
DB_URL=postgresql+psycopg2://user:password@host:5432/dbname
```

`psycopg2-binary` is already included as a dependency.

## Docker

```bash
docker build -t ai-use-philosophy .
docker run -p 8000:8000 --env-file .env ai-use-philosophy
```

## Deployment

The included `Dockerfile` is deployment-ready and is what runs the hosted
instance on [Render](https://render.com) at
https://ai-use-philosophy.onrender.com/mcp. On hosts with ephemeral filesystems
(e.g. Render's free tier) the SQLite file does not persist across restarts —
point `DB_URL` at a managed PostgreSQL instance instead.

## Connecting a client

Point an MCP client at the server's `/mcp` endpoint — the hosted instance:

```json
{
  "mcpServers": {
    "ai-use-philosophy": {
      "url": "https://ai-use-philosophy.onrender.com/mcp"
    }
  }
}
```

or a local run at `http://localhost:8000/mcp`.

## Project layout

```
src/ai_use_philosophy/
├── __init__.py     # entrypoint: runs the MCP server (streamable-http)
├── server.py       # MCP server: prompt + tool definitions, "/" landing route
├── homepage.py     # plain-text setup page served at "/"
├── repository.py   # PrincipleRepository — CRUD over the database
├── models.py       # SQLAlchemy model (Principle)
├── schemas.py      # Pydantic output schema (PrincipleOut)
├── db.py           # engine / table bootstrap
├── config.py       # pydantic-settings configuration
└── logger.py       # logging setup
```
