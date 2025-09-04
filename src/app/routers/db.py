from flask import Blueprint
from sqlalchemy import text

from src.app.repositories.db import engine, session_factory
from src.app.repositories.sqlalchemy_video_repo import SqlAlchemyVideoRepo

db = Blueprint("db", __name__)


@db.route("/connect", methods=["GET"])
def connect():
    video_repo = SqlAlchemyVideoRepo(session_factory)
    try:
        with engine.connect() as c:
            c.execute(text("SELECT 1"))
    except Exception as e:
        return {"error": str(e)}, 500
    return {"response": "healthy"}, 200
