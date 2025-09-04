from typing import Protocol, Iterable, Optional, List

from ..domain.video import Video


class VideoRepo(Protocol):
    def save(self, v: Video) -> None: ...
    def get(self, video_id: str) -> Optional[Video]: ...
    def list(self, limit: int = 50, offset: int = 0) -> Iterable[Video]: ...
    def delete(self, video_id: str) -> None: ...


class InMemoryVideoRepo(Video):
    def __init__(self) -> None:
        self._store: dict[str, Video] = {}

    def save(self, v: Video) -> None:
        self._store[str(v.id)] = v

    def get(self, video_id: str) -> Optional[Video]:
        return self._store.get(video_id)

    def list(self, limit: int = 50, offset: int = 0) -> List[Video]:
        values = list(self._store.values())
        return values[offset : offset + limit]

    def delete(self, video_id: str) -> None:
        self._store.pop(video_id, None)
