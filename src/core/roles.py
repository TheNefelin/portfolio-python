"""Vocabulario de roles del sistema (contrato con la BD).

Un solo rol por fuente de verdad:
- El catálogo real vive en la tabla `user_roles` (datos).
- Este enum es el CONTRATO que el código usa para nombrarlos (evita strings
  mágicos) y debe coincidir con el seed de `postgre_auth.sql`.
- `core/startup.py` valida al arrancar que estos valores existan en la BD;
  si divergen, la app NO arranca (fail-fast).
"""

from enum import Enum


class UserRole(str, Enum):
  ADMIN = "admin"
  USER = "user"