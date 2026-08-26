from sqlalchemy import create_engine

from ai_use_philosophy.logger import logger
from ai_use_philosophy.models import Base

logger.info("Creating database engine: sqlite:///principles.db")
engine = create_engine("sqlite:///principles.db")
Base.metadata.create_all(engine)  # creates the table if it doesn't exist
logger.info("Database tables ensured")
