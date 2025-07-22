from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://chart_analyzer_user:chartanalyzer13@localhost:5432/chart_analyzer"
    JWT_SECRET: str = "a_very_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()