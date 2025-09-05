import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Video:
    id: uuid.UUID = uuid.uuid4()
    prompt: str = ""
    title: str = ""
    description: str = ""
    summary: str = ""
    script: str = ""
    url: str = ""
    duration: float = 0.0
    views: int = 0
    created_at: datetime = datetime.now()
