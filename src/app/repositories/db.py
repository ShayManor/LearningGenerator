from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import sessionmaker, Session
import os

DB_URL: str = os.getenv("SUPABASE_DB_URL") or ""

if not DB_URL:
    raise ValueError("SUPABASE_DB_URL environment variable NOT set.")

# PgBouncer already pools, so use NullPool.
engine = create_engine(
    DB_URL,
    poolclass=NullPool,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# convenient dependency/factory
def session_factory() -> Session:
    return SessionLocal()
