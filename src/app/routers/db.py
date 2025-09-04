import sqlalchemy
from flask import Blueprint
from sqlalchemy import text

from src.app.repositories.db import engine, session_factory
from src.app.repositories.sqlalchemy_video_repo import SqlAlchemyVideoRepo

db = Blueprint("db", __name__)


@db.route("/connect", methods=["GET"])
def connect():
    video_repo = SqlAlchemyVideoRepo(session_factory)
    print(video_repo.list())
    try:
        with engine.connect() as c:
            res: sqlalchemy.engine.cursor.CursorResult = c.execute(
                text("SELECT COUNT(*) FROM public.videos")
            )
            row = res.fetchone()
    except Exception as e:
        return {"error": str(e)}, 500
    return {"response": row[0]}, 200
