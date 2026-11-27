"""Startup validation for the portfolio API.

Validates that the database catalog matches the application's contracts
(e.g., roles defined in `core/roles.py` exist in `user_roles`).
If a contract is violated, the app fails to start (fail-fast).
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .roles import UserRole
from ..models.auth_models import UserRole as UserRoleModel


async def validate_roles(db: AsyncSession) -> None:
  """Verify that all roles in the UserRole enum exist in the database.

  Raises RuntimeError if any role is missing.
  """
  for role in UserRole:
    result = await db.execute(
      select(UserRoleModel).where(UserRoleModel.name == role.value)
    )
    if result.scalar_one_or_none() is None:
      raise RuntimeError(
        f"Seed faltante: no existe el rol '{role.value}' en user_roles. "
        f"Ejecuta postgre_auth.sql para poblar la BD."
      )