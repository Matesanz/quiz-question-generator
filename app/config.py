"""Configuration settings for the Quiz Question Generator API."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Configuration class for the API and LLM settings."""

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # LLM Config
    OPENAI_API_KEY: str
    LLM_MODEL: str = "openai:gpt-4o-mini-2024-07-18"

    # API Config
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_DEBUG: bool = False

app_config = Config()
