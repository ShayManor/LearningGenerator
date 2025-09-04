from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv("SUPABASE_DB_URL")


# PgBouncer already pools, so use NullPool.
engine = create_engine(
    DB_URL,
    poolclass=NullPool,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# convenient dependency/factory
def session_factory():
    return SessionLocal()
