from datetime import datetime
from typing import Optional, Iterable, Callable

from sqlalchemy.orm import Session  # noqa: F401

from ..domain.video import Video
from .video_repo import VideoRepo
from .tables import VideoRow  # SQLAlchemy Table / Declarative model


class SqlAlchemyVideoRepo(VideoRepo):
    def __init__(self, session_factory: Callable[[], Session]) -> None:
        self._session_factory = session_factory

    def save(self, v: Video) -> None:
        with self._session_factory() as s:  # type: Session
            row = s.get(Video, v.id) or Video(id=v.id)
            row.title = v.title
            row.summary = v.summary
            row.script = v.script
            row.url = v.url
            row.duration = v.duration
            row.views = v.views
            row.created_at = v.created_at
            s.add(row)
            s.commit()

    def get(self, video_id: str) -> Optional[Video]:
        with self._session_factory() as s:
            row = s.get(Video, video_id)
            if not row:
                return None
            return Video(
                id=row.id,
                title=row.title,
                summary=row.summary,
                script=row.script,
                url=row.url,
                duration=row.duration,
                views=row.views,
                created_at=row.created_at,
            )

    def list(self, limit: int = 50, offset: int = 0) -> Iterable[Video]:
        with self._session_factory() as s:
            q = (
                s.query(VideoRow)
                .order_by(VideoRow.created_at.desc())
                .offset(offset)
                .limit(limit)
            )
            return [
                Video(
                    id=r.id.as_uuid,
                    title=str(r.title),
                    summary=str(r.summary),
                    script=str(r.script),
                    url=str(r.url),
                    duration=float(r.duration),
                    views=int(r.views),
                    created_at=datetime(
                        r.created_at.year, r.created_at.month, r.created_at.day
                    ),
                )
                for r in q.all()
            ]

    def delete(self, video_id: str) -> None:
        with self._session_factory() as s:
            row = s.get(VideoRow, video_id)
            if row:
                s.delete(row)
                s.commit()
