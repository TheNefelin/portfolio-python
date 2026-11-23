"""Verificación de identity tokens de Apple Sign In.

Apple emite un identity token (JWT) firmado con RS256. El backend lo verifica
contra las claves públicas de Apple (JWKS en https://appleid.apple.com/auth/keys).

Reglas de aceptación:
- Firma válida (RS256) contra una clave de Apple.
- iss == https://appleid.apple.com
- aud == APPLE_CLIENT_ID (Services ID o App ID)
- exp no expirado
- email presente (Apple lo incluye en el token)

Devuelve los claims del token o None si no es válido.
"""

import httpx
from jose import jwk, jwt
from jose.exceptions import JOSEError

from src.core.config import settings

_TIMEOUT_SECONDS = 10.0
_APPLE_JWKS_URL = "https://appleid.apple.com/auth/keys"


async def _fetch_apple_keys() -> dict | None:
  """Obtiene las claves públicas de Apple (JWKS)."""
  try:
    async with httpx.AsyncClient(timeout=_TIMEOUT_SECONDS) as client:
      response = await client.get(settings.APPLE_JWKS_URL or _APPLE_JWKS_URL)
  except httpx.HTTPError:
    return None

  if response.status_code != 200:
    return None

  return response.json()


async def verify_apple_token(token: str) -> dict | None:
  if not token:
    return None

  if not settings.APPLE_CLIENT_ID:
    return None  # Apple login desactivado

  # Obtener las claves públicas de Apple
  jwks = await _fetch_apple_keys()
  if not jwks or "keys" not in jwks:
    return None

  # Extraer el header del token para obtener el kid
  try:
    unverified_header = jwt.get_unverified_header(token)
  except JOSEError:
    return None

  kid = unverified_header.get("kid")
  alg = unverified_header.get("alg", "RS256")

  if not kid:
    return None

  # Buscar la clave correspondiente
  key_data = None
  for key in jwks["keys"]:
    if key.get("kid") == kid:
      key_data = key
      break

  if not key_data:
    return None

  # Construir la clave pública RSA
  try:
    public_key = jwk.construct(key_data)
  except JOSEError:
    return None

  # Verificar el token
  try:
    claims = jwt.decode(
      token,
      public_key,
      algorithms=[alg],
      audience=settings.APPLE_CLIENT_ID,
      issuer=settings.APPLE_ISSUER,
      options={"verify_exp": True, "verify_aud": True, "verify_iss": True},
    )
  except JOSEError:
    return None

  # Verificar que tenga email
  email = claims.get("email")
  if not email:
    return None

  # Apple solo envía el nombre en el primer login (vía el parámetro "user" en el frontend).
  # El identity token no incluye nombre. Se maneja en el service.

  return {
    "sub": claims.get("sub"),
    "email": email,
    "email_verified": claims.get("email_verified", True),
    "name": None,  # Apple no envía nombre en el token
    "given_name": None,
    "family_name": None,
    "lastname": None,
    "picture": None,
  }


async def fetch_apple_userinfo(token: str) -> dict | None:
  """Apple no tiene un endpoint de userinfo. El perfil viene en el token."""
  return await verify_apple_token(token)