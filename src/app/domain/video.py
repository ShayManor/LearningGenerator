import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Video:
    id: uuid.UUID = uuid.uuid4()
    prompt: Optional[str] = None
    title: str = ""
    summary: str = ""
    script: str = ""
    url: str = ""
    duration: float = 0.0
    views: int = 0
    created_at: datetime = datetime.now()
