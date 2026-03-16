"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Central settings object – populated from env vars / .env file."""

    # ── Database ─────────────────────────────────────────────
    database_url: str = "postgresql+asyncpg://tailorflow:tailorflow@localhost:5433/tailorflow"

    # ── Auth / JWT ───────────────────────────────────────────
    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # ── OpenAI ───────────────────────────────────────────────
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"

    # ── File Storage ─────────────────────────────────────────
    upload_dir: str = "./uploads"
    max_upload_size_mb: int = 10

    # ── LaTeX ────────────────────────────────────────────────
    latex_compile_timeout_seconds: int = 60

    # ── App ──────────────────────────────────────────────────
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: str = "http://localhost:3001"
    environment: str = "development"

    @property
    def cors_origins_list(self) -> list[str]:
        """Parse comma-separated CORS origins into a list."""
        return [origin.strip() for origin in self.cors_origins.split(",")]

    model_config = {"env_file": ["../../.env", ".env"], "env_file_encoding": "utf-8", "extra": "ignore"}


settings = Settings()
