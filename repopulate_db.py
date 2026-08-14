"""
Rebuild a PostgreSQL database for this project from the SQL files.

Usage:
  python repopulate_db.py [--force] [--test]

  --force   Drop and recreate the target database before applying schema + seed.
  --test    Use TEST_DATABASE_URL instead of DATABASE_URL.

The connection string is read from .env (via python-dotenv). Requires a running
PostgreSQL server. The .sql files already start a transaction, so execution is
atomic per file.
"""

import argparse
import asyncio
import os
import sys
from pathlib import Path

import asyncpg
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = BASE_DIR / "postgre_schema.sql"
SEED_FILE = BASE_DIR / "postgre_seed.sql"


def _normalize(url: str) -> str:
  """asyncpg expects a 'postgresql'/'postgres' scheme, not SQLAlchemy's 'postgresql+asyncpg'."""
  return url.replace("postgresql+asyncpg://", "postgresql://", 1)


def _admin_url(url: str) -> str:
  """Return the URL of the same server, connected to the maintenance 'postgres' DB."""
  return _normalize(url).rsplit("/", 1)[0] + "/postgres"


async def _drop_and_create(url: str) -> None:
  admin = _admin_url(url)
  conn = await asyncpg.connect(admin)
  try:
    db_name = url.rsplit("/", 1)[1]
    rows = await conn.fetch("SELECT pid, pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = $1 AND pid <> pg_backend_pid()", db_name)
    print(f"Terminated {len(rows)} connection(s) to '{db_name}'.")
    await conn.execute(f'DROP DATABASE IF EXISTS "{db_name}"')
    await conn.execute(f'CREATE DATABASE "{db_name}"')
    print(f"Database '{db_name}' recreated.")
  finally:
    await conn.close()


async def _apply_file(conn: asyncpg.Connection, path: Path, label: str) -> None:
  sql = path.read_text(encoding="utf-8")
  await conn.execute(sql)
  print(f"Applied {label}: {path.name}")


async def main() -> int:
  parser = argparse.ArgumentParser(description="Rebuild the portfolio database from SQL files.")
  parser.add_argument("--force", action="store_true", help="Drop and recreate the database first.")
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

  if args.force:
    await _drop_and_create(url)

  conn = await asyncpg.connect(url)
  try:
    await _apply_file(conn, SCHEMA_FILE, "schema")
    await _apply_file(conn, SEED_FILE, "seed")
  finally:
    await conn.close()

  print("Done. Database rebuilt.")
  return 0


if __name__ == "__main__":
  raise SystemExit(asyncio.run(main()))