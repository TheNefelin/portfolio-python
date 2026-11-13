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

  # Google OAuth. Solo CLIENT_ID, TOKEN_INFO_URL y USERINFO_URL se usan realmente
  # (google_service.py). Las demas (client_secret, issuer, scope) no se usan hoy:
  # el login usa el flujo implicit de GIS y valida aud + email_verified en tokeninfo.
  GOOGLE_CLIENT_ID: str = ""
  GOOGLE_TOKEN_INFO_URL: str = "https://oauth2.googleapis.com/tokeninfo"
  GOOGLE_USERINFO_URL: str = "https://www.googleapis.com/oauth2/v3/userinfo"

  @property
  def cors_origins_list(self) -> list[str]:
    raw = self.CORS_ORIGINS.strip()
    if not raw:
      return []
    return json.loads(raw)

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
    extra="ignore",
  )


settings = Settings()
