from typing import Optional

import sqlalchemy
from flask import Blueprint, Response, jsonify
from sqlalchemy import text, Row

from src.app.repositories.db import engine, session_factory
from src.app.repositories.sqlalchemy_video_repo import SqlAlchemyVideoRepo

db = Blueprint("db", __name__)


@db.route("/connect", methods=["GET"])
def connect() -> Response:
    video_repo = SqlAlchemyVideoRepo(session_factory)
    print(video_repo.list())
    try:
        with engine.connect() as c:
            res: sqlalchemy.engine.cursor.CursorResult = c.execute(
                text("SELECT COUNT(*) FROM public.videos")
            )
            row: Optional[Row] = res.fetchone()
            if not row:
                return jsonify({"Connection successful but no rows found"}, 200)
            return jsonify({"response": row[0]}, 200)
    except Exception as e:
        return jsonify({"error": str(e)}, 500)
