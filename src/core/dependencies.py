"""Dependencias transversales de la API (API Key del BFF).

Fachada: la implementación vive en `core.security` (única fuente de verdad).
Aquí solo se reexporta para que los routers sigan importando desde
`src.core.dependencies` sin cambiar sus imports.
"""

from src.core.security import verify_api_key

__all__ = ["verify_api_key"]
