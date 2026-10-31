import json

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  DEBUG: bool = False

  DATABASE_URL: str
  TEST_DATABASE_URL: str | None = None

  CORS_ORIGINS: str
  API_KEY: str

  TOKEN_SECRET_KEY: str
  TOKEN_ACCESS_EXPIRE_MINUTES: int = 15
  TOKEN_REFRESH_EXPIRE_DAYS: int = 1

  CLOUDINARY_CLOUD_NAME: str
  CLOUDINARY_API_KEY: str
  CLOUDINARY_API_SECRET: str

  GOOGLE_CLIENT_ID: str | None = None
  GOOGLE_CLIENT_SECRET: str | None = None

  GITHUB_CLIENT_ID: str | None = None
  GITHUB_CLIENT_SECRET: str | None = None

  APPLE_CLIENT_ID: str | None = None
  APPLE_CLIENT_SECRET: str | None = None

  @property
  def cors_origins_list(self) -> list[str]:
    return json.loads(self.CORS_ORIGINS)

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
    extra="ignore",
  )


settings = Settings()
