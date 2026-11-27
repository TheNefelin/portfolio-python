"""
Rebuild a PostgreSQL database for this project from the SQL files.

Usage:
  python repopulate_db.py [--test]

  --test    Use TEST_DATABASE_URL instead of DATABASE_URL.

The connection string is read from .env (via python-dotenv). Requires a running
PostgreSQL server. The .sql files already start a transaction, so execution is
atomic per file.

NOTE: This script only applies the .sql files (CREATE TABLE IF NOT EXISTS +
seeds idempotentes). It does NOT create, drop or modify the database or tables.
If the database does not exist, create it manually first.
"""

import argparse
import os
import sys
from pathlib import Path

import asyncpg
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = BASE_DIR / "postgre_schema.sql"
SEED_FILE = BASE_DIR / "postgre_seed.sql"
AUTH_SCHEMA_FILE = BASE_DIR / "postgre_auth.sql"


def _normalize(url: str) -> str:
  """asyncpg expects a 'postgresql'/'postgres' scheme, not SQLAlchemy's 'postgresql+asyncpg'."""
  return url.replace("postgresql+asyncpg://", "postgresql://", 1)


async def _apply_file(conn: asyncpg.Connection, path: Path, label: str) -> None:
  sql = path.read_text(encoding="utf-8")
  await conn.execute(sql)
  print(f"Applied {label}: {path.name}")


async def main() -> int:
  parser = argparse.ArgumentParser(description="Rebuild the portfolio database from SQL files.")
  parser.add_argument("--test", action="store_true", help="Use TEST_DATABASE_URL instead of DATABASE_URL.")
  args = parser.parse_args()

  load_dotenv(BASE_DIR / ".env")
  url = os.getenv("TEST_DATABASE_URL" if args.test else "DATABASE_URL")
  if not url:
    print("ERROR: DATABASE_URL is not defined in .env.", file=sys.stderr)
    return 1
  url = _normalize(url)

  for file, label in ((SCHEMA_FILE, "schema"), (SEED_FILE, "seed")):
    if not file.exists():
      print(f"ERROR: {file.name} not found in {BASE_DIR}.", file=sys.stderr)
      return 1

  conn = await asyncpg.connect(url)
  try:
    await _apply_file(conn, SCHEMA_FILE, "schema")
    if AUTH_SCHEMA_FILE.exists():
      await _apply_file(conn, AUTH_SCHEMA_FILE, "auth schema")
    await _apply_file(conn, SEED_FILE, "seed")
  finally:
    await conn.close()

  print("Done. Database rebuilt.")
  return 0


if __name__ == "__main__":
  import asyncio
  raise SystemExit(asyncio.run(main()))