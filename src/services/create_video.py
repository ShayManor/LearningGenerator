from typing import Tuple

from src.app.domain.llm import Tool
from src.app.domain.video import Video
from src.app.gateways.llm.llm_client import LLMClient
from src.app.gateways.storage.storage import Storage
from src.app.repositories.video_repo import VideoRepo


class CreateVideoService:
    def __init__(self, repo: VideoRepo, llm: LLMClient, store: Storage):
        self.repo = repo
        self.llm = llm
        self.store = store
        self.v = None

    def execute(self, prompt: str) -> Video:
        if not prompt:
            raise ValueError("Prompt is required")

        self.v = Video()

        self.v.title = self._make_title()
        self.v.desc = self._make_description()
        self.v.script = self._make_script()
        self.v.summary = self._make_summary()

        self.v.url, self.v.duration = self._upload_rendered()
        self.v.views = 0

        self.repo.save(self.v)
        return self.v

    def _make_title(self) -> str:
        if not self.v.prompt:
            raise RuntimeError("Prompt not set, can't fill title")
        title = self.llm.call_llm(
            prompt=self.v.prompt,
            model="gpt-4.1-mini-2025-04-14",
            system="create_video_title",
        )
        return title

    def _make_description(self) -> str:
        if not self.v.prompt:
            raise RuntimeError("Prompt not set, can't fill description")
        if not self.v.title:
            raise RuntimeError("Title not set, can't fill description")
        desc = self.llm.call_llm(
            prompt=f"Prompt: {self.v.prompt}\n\nTitle: {self.v.title}",
            model="gpt-5-mini",
            system="create_video_desc",
        )
        print(desc)
        return desc

    def _make_script(self) -> str:
        if not self.v.title:
            raise RuntimeError("Title not set, can't fill title")
        if not self.v.description:
            raise RuntimeError("Description not set, can't fill title")
        if not self.v.prompt:
            raise RuntimeError("Prompt not set, can't fill title")

        web_tool = Tool()
        web_tool.WEB_SEARCH = True
        script = self.llm.call_llm(
            prompt=f"Prompt: {self.v.prompt}\n\nTitle: {self.v.title}\n\nDescription: {self.v.description}",
            model="gpt-5",
            system="create_video_script",
            tools=web_tool,
        )
        return script

    def _make_summary(self) -> str:
        if not self.v.script:
            raise RuntimeError("Script not set, can't fill title")
        return "Example"

    def _upload_rendered(self) -> Tuple[str, float]:
        """
        Uploads video to bucket and returns url, duration
        :return: url for video
        """
        return "https://", 1.1
