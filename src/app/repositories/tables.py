from sqlalchemy import Column, String, Integer, DateTime, Float, UUID
from sqlalchemy.orm import DeclarativeBase
import datetime


class Base(DeclarativeBase):  # SQLAlchemy-2.0 style base
    pass


class VideoRow(Base):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    script = Column(String, nullable=True)
    url = Column(String, nullable=True)
    duration = Column(Float, nullable=True)
    prompt = Column(String, nullable=True)
    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now())
