from dataclasses import dataclass
from uuid import uuid4

from src.models.create_video import BaseVideo


#     id: uuid.UUID = uuid4()
#     prompt: Optional[str] = None
#     title: str = ""
#     summary: str = ""
#     script: str = ""
#     url: str = ""
#     duration: float = 0.0
#     views: int = 0
@dataclass
class Video(BaseVideo):
    def _set_title(self):
        if not self.prompt:
            raise RuntimeError("Prompt not set, can't fill title")
        self.script = ""

    def _set_summary(self):
        if not self.script:
            raise RuntimeError("Script not set, can't fill title")

    def _set_script(self):
        if not self.prompt:
            raise RuntimeError("Prompt not set, can't fill title")


    def _upload(self) -> str:
        """
        Uploads video to bucket and sets url, duration
        :return: url for video
        """
        pass

    def create_video(self, prompt):
        self.id = uuid4()
        self.prompt = prompt
        self.views = 0
