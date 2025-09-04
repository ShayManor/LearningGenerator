from sqlalchemy import Column, String, Integer, DateTime, Uuid, BaseRow, Float
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()


class VideoRow(BaseRow):
    __tablename__ = "videos"

    id = Column(Uuid, primary_key=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    script = Column(String, nullable=True)
    url = Column(String, nullable=True)
    duration = Column(Float, nullable=True)
    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
