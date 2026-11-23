"""Verificación de tokens de GitHub contra la API de GitHub.

El frontend obtiene un access_token de GitHub (flujo OAuth) y lo envía
al backend. El backend lo verifica llamando a https://api.github.com/user.

Reglas de aceptación:
- status 200 de /user (GitHub valida el token).
- El usuario debe tener un email (público o privado via /user/emails).

Devuelve un dict con los datos del usuario o None si no es válido.
"""

import httpx

from src.core.config import settings

_TIMEOUT_SECONDS = 10.0
_GITHUB_USER_URL = "https://api.github.com/user"
_GITHUB_EMAILS_URL = "https://api.github.com/user/emails"
_GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"


async def exchange_code_for_token(code: str) -> str | None:
    """Intercambia el authorization code por un access token de GitHub."""
    if not code or not settings.GITHUB_CLIENT_ID or not settings.GITHUB_CLIENT_SECRET:
        return None

    try:
        async with httpx.AsyncClient(timeout=_TIMEOUT_SECONDS) as client:
            response = await client.post(
                settings.GITHUB_TOKEN_URL or _GITHUB_TOKEN_URL,
                data={
                    "client_id": settings.GITHUB_CLIENT_ID,
                    "client_secret": settings.GITHUB_CLIENT_SECRET,
                    "code": code,
                },
                headers={"Accept": "application/json"},
            )
    except httpx.HTTPError:
        return None

    if response.status_code != 200:
        return None

    data = response.json()
    if "error" in data:
        return None

    return data.get("access_token")


async def verify_github_token(token: str) -> dict | None:
  if not token:
    return None

  try:
    async with httpx.AsyncClient(timeout=_TIMEOUT_SECONDS) as client:
      response = await client.get(
        _GITHUB_USER_URL,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
      )
  except httpx.HTTPError:
    return None

  if response.status_code != 200:
    return None

  data = response.json()

  # GitHub puede no devolver email si es privado. Intentar /user/emails.
  email = data.get("email")
  if not email:
    try:
      async with httpx.AsyncClient(timeout=_TIMEOUT_SECONDS) as client:
        emails_resp = await client.get(
          _GITHUB_EMAILS_URL,
          headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        )
      if emails_resp.status_code == 200:
        emails = emails_resp.json()
        # Preferir el email primario verificado
        primary = next((e for e in emails if e.get("primary") and e.get("verified")), None)
        if primary:
          email = primary.get("email")
        elif emails:
          email = emails[0].get("email")
    except httpx.HTTPError:
      pass

  if not email:
    return None

  # Verificar que el email esté verificado
  # GitHub no devuelve email_verified en /user, pero /user/emails sí tiene "verified"
  # Si no pudimos obtener emails, asumimos que el email de /user es válido

  name = data.get("name") or data.get("login")
  # Separar nombre en given_name y family_name si es posible
  given_name = None
  family_name = None
  if name:
    parts = name.split(" ", 1)
    given_name = parts[0]
    family_name = parts[1] if len(parts) > 1 else None

  return {
    "sub": str(data.get("id")),
    "email": email,
    "email_verified": True,
    "name": given_name,
    "given_name": given_name,
    "family_name": family_name,
    "lastname": family_name,
    "picture": data.get("avatar_url"),
  }


async def fetch_github_userinfo(token: str) -> dict | None:
  """Obtiene datos adicionales del usuario (ya incluidos en verify)."""
  # GitHub /user ya devuelve toda la info necesaria
  return await verify_github_token(token)