import json

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  DEBUG: bool = False

  DATABASE_URL: str
  TEST_DATABASE_URL: str | None = None

  CLOUDINARY_CLOUD_NAME: str
  CLOUDINARY_API_KEY: str
  CLOUDINARY_API_SECRET: str

  CORS_ORIGINS: str
  API_KEY: str

  JWT_SECRET_KEY: str
  JWT_ALGORITHM: str = "HS256"
  JWT_ACCESS_EXPIRE_MINUTES: int = 15
  JWT_REFRESH_EXPIRE_DAYS: int = 1
  JWT_REFRESH_IDLE_MINUTES: int = 30

  GOOGLE_CLIENT_ID: str
  GOOGLE_CLIENT_SECRET: str
  GOOGLE_TOKEN_INFO_URL: str
  GOOGLE_USERINFO_URL: str
  GOOGLE_ISSUER: str
  GOOGLE_SCOPE: str

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
