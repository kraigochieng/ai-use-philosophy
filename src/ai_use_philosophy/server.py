# server.py
from mcp.server import MCPServer

from ai_use_philosophy.config import settings
from ai_use_philosophy.logger import logger
from ai_use_philosophy.repository import PrincipleRepository
from ai_use_philosophy.schemas import PrincipleOut

mcp = MCPServer("ai-use-philosophy")
repo = PrincipleRepository(db_url=settings.db_url)


@mcp.prompt()
def apply_all_principles() -> str:
    """Load and apply every stored principle for this conversation."""
    logger.info("Prompt call: apply_all_principles")
    principles = repo.get_all()
    text = "\n".join(f"- {p.principle}" for p in principles)
    return f"Apply the following principles to everything in this conversation:\n{text}"


@mcp.tool()
def add_principle(text: str) -> str:
    """Add a new principle to the store."""
    logger.info(f"Tool call: add_principle(text={text!r})")
    repo.add(text)
    return f"Added: {text}"


@mcp.tool()
def list_principles() -> list[PrincipleOut]:
    """List all stored AI-use principles with their ids."""
    logger.info("Tool call: list_principles")
    return repo.get_all()


@mcp.tool()
def edit_principle(principle_id: int, new_text: str) -> str:
    """Edit an existing principle by id."""
    logger.info(f"Tool call: edit_principle(id={principle_id})")
    success = repo.update(principle_id, new_text)
    return (
        f"Updated principle {principle_id}"
        if success
        else f"No principle found with id {principle_id}"
    )


@mcp.tool()
def delete_principle(principle_id: int) -> str:
    """Delete a principle by id."""
    logger.info(f"Tool call: delete_principle(id={principle_id})")
    success = repo.delete(principle_id)
    return (
        f"Deleted principle {principle_id}"
        if success
        else f"No principle found with id {principle_id}"
    )


# if __name__ == "__main__":
#     logger.info(f"Starting MCP server on {settings.host}:{settings.port}")
#     mcp.run(
#         transport="streamable-http", host=settings.host, port=settings.port, path="/mcp"
#     )
