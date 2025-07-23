# src/config.py
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://chart_analyzer_user:chartanalyzer13@localhost:5432/chart_analyzer"
    JWT_SECRET: str = "a_very_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30

    # Use model_config instead of inner Config class
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # or "allow" if you want to allow extra fields
    )

settings = Settings()