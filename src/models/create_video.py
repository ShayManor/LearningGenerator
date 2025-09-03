import uuid
from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class BaseVideo:
    id: uuid.UUID = uuid4()
    prompt: Optional[str] = None
    title: str = ""
    summary: str = ""
    script: str = ""
    url: str = ""
    duration: float = 0.0
    views: int = 0
