# homepage.py
"""Plain-text landing page served at ``/`` with setup directions."""

PUBLIC_URL = "https://ai-use-philosophy.onrender.com/mcp"

HOMEPAGE_TEXT = f"""\
AI USE PHILOSOPHY
=================

An MCP server that stores your personal "AI-use philosophy" -- a running list of
principles for how you want AI assistants to behave -- and serves them to any
MCP client so they can be loaded and applied to a conversation.


ENDPOINT
--------

  {PUBLIC_URL}

Streamable-HTTP transport. This page lives at "/"; the MCP protocol is at "/mcp".


CONNECT A CLIENT
----------------

Point any MCP client that speaks streamable-HTTP at the endpoint above:

  {{
    "mcpServers": {{
      "ai-use-philosophy": {{
        "url": "{PUBLIC_URL}"
      }}
    }}
  }}

Claude Code:

  claude mcp add --transport http ai-use-philosophy {PUBLIC_URL}

Claude Desktop / stdio-only clients (bridge over mcp-remote):

  {{
    "mcpServers": {{
      "ai-use-philosophy": {{
        "command": "npx",
        "args": ["-y", "mcp-remote", "{PUBLIC_URL}"]
      }}
    }}
  }}


WHAT THE SERVER EXPOSES
-----------------------

  prompt  apply_all_principles  Load and apply every stored principle.
  tool    add_principle         Add a new principle.
  tool    list_principles       List all principles with their ids.
  tool    edit_principle        Replace the text of a principle by id.
  tool    delete_principle      Delete a principle by id.


RUN IT LOCALLY
--------------

  git clone https://github.com/kraigochieng/ai-use-philosophy.git
  cd ai-use-philosophy
  uv sync
  cp .env.example .env
  uv run ai-use-philosophy

The server then listens on http://0.0.0.0:8000/mcp. Configure it with the PORT,
HOST, and DB_URL environment variables.

Source: https://github.com/kraigochieng/ai-use-philosophy
"""
