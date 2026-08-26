from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from ai_use_philosophy.logger import logger

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    port: int = 8000
    host: str = "0.0.0.0"

    model_config = SettingsConfigDict(env_prefix="", case_sensitive=False)

settings = Settings()
logger.info(f"Settings loaded: host={settings.host}, port={settings.port}")