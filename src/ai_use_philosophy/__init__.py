from ai_use_philosophy.config import settings
from ai_use_philosophy.logger import logger
from ai_use_philosophy.server import mcp


def main() -> None:
    logger.info("Starting ai-use-philosophy")
    mcp.run(
        transport="streamable-http",
        host=settings.host,
        port=settings.port,
        streamable_http_path="/mcp",
    )
