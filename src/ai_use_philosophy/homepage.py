# homepage.py
"""Static landing page served at ``/`` with setup directions."""

PUBLIC_URL = "https://ai-use-philosophy.onrender.com/mcp"

HOMEPAGE_HTML = f"""\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Use Philosophy &middot; MCP Server</title>
<style>
  :root {{
    color-scheme: light dark;
    --bg: #ffffff;
    --fg: #1a1a1a;
    --muted: #5b5b5b;
    --border: #e2e2e2;
    --code-bg: #f5f5f5;
    --accent: #3b5bdb;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #16181d;
      --fg: #e8e8e8;
      --muted: #9aa0a6;
      --border: #2c2f36;
      --code-bg: #1f2228;
      --accent: #8ea2ff;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 2.5rem 1.25rem 4rem;
    background: var(--bg);
    color: var(--fg);
    font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  main {{ max-width: 46rem; margin: 0 auto; }}
  h1 {{ font-size: 1.7rem; margin: 0 0 0.25rem; }}
  h2 {{ font-size: 1.15rem; margin: 2.25rem 0 0.75rem; }}
  p {{ margin: 0.75rem 0; }}
  .lede {{ color: var(--muted); margin-top: 0; }}
  a {{ color: var(--accent); }}
  code {{
    background: var(--code-bg);
    padding: 0.1rem 0.35rem;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  }}
  pre {{
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    overflow-x: auto;
  }}
  pre code {{ background: none; padding: 0; font-size: 0.85rem; }}
  table {{ border-collapse: collapse; width: 100%; margin: 0.75rem 0; }}
  th, td {{ text-align: left; padding: 0.5rem 0.75rem; border-bottom: 1px solid var(--border); }}
  th {{ color: var(--muted); font-weight: 600; }}
  .endpoint {{
    display: inline-block;
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.4rem 0.7rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.9rem;
  }}
  footer {{ margin-top: 3rem; color: var(--muted); font-size: 0.85rem; }}
</style>
</head>
<body>
<main>
  <h1>AI Use Philosophy</h1>
  <p class="lede">
    An MCP server that stores your personal &ldquo;AI-use philosophy&rdquo; &mdash; a
    running list of principles for how you want AI assistants to behave &mdash; and
    serves them to any MCP client so they can be loaded and applied to a conversation.
  </p>

  <h2>Endpoint</h2>
  <p><span class="endpoint">{PUBLIC_URL}</span></p>
  <p>Streamable-HTTP transport. This page lives at <code>/</code>; the MCP protocol is served at <code>/mcp</code>.</p>

  <h2>Connect a client</h2>
  <p>Point any MCP client that speaks streamable-HTTP at the endpoint above:</p>
  <pre><code>{{
  "mcpServers": {{
    "ai-use-philosophy": {{
      "url": "{PUBLIC_URL}"
    }}
  }}
}}</code></pre>

  <h3 style="font-size:1rem;margin:1.25rem 0 0.4rem;">Claude Code</h3>
  <pre><code>claude mcp add --transport http ai-use-philosophy {PUBLIC_URL}</code></pre>

  <h3 style="font-size:1rem;margin:1.25rem 0 0.4rem;">Claude Desktop / stdio-only clients</h3>
  <p>Bridge over <code>mcp-remote</code> if the client cannot do HTTP directly:</p>
  <pre><code>{{
  "mcpServers": {{
    "ai-use-philosophy": {{
      "command": "npx",
      "args": ["-y", "mcp-remote", "{PUBLIC_URL}"]
    }}
  }}
}}</code></pre>

  <h2>What the server exposes</h2>
  <table>
    <thead><tr><th>Kind</th><th>Name</th><th>Description</th></tr></thead>
    <tbody>
      <tr><td>Prompt</td><td><code>apply_all_principles</code></td><td>Load and apply every stored principle for the conversation.</td></tr>
      <tr><td>Tool</td><td><code>add_principle</code></td><td>Add a new principle.</td></tr>
      <tr><td>Tool</td><td><code>list_principles</code></td><td>List all principles with their ids.</td></tr>
      <tr><td>Tool</td><td><code>edit_principle</code></td><td>Replace the text of a principle by id.</td></tr>
      <tr><td>Tool</td><td><code>delete_principle</code></td><td>Delete a principle by id.</td></tr>
    </tbody>
  </table>

  <h2>Run it locally</h2>
  <pre><code>git clone https://github.com/kraigochieng/ai-use-philosophy.git
cd ai-use-philosophy
uv sync
cp .env.example .env
uv run ai-use-philosophy</code></pre>
  <p>The server then listens on <code>http://0.0.0.0:8000/mcp</code>. Configure it with the
  <code>PORT</code>, <code>HOST</code>, and <code>DB_URL</code> environment variables.</p>

  <footer>
    Source: <a href="https://github.com/kraigochieng/ai-use-philosophy">github.com/kraigochieng/ai-use-philosophy</a>
  </footer>
</main>
</body>
</html>
"""
