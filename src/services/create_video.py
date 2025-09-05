from dataclasses import replace
from typing import Tuple

from src.app.domain.video import Video
from src.app.gateways.llm.llm_client import LLMClient
from src.app.gateways.storage.storage import Storage
from src.app.repositories.video_repo import VideoRepo


class CreateVideoService:
    def __init__(self, repo: VideoRepo, llm: LLMClient, store: Storage):
        self.repo = repo
        self.llm = llm
        self.store = store

    def execute(self, prompt: str) -> Video:
        if not prompt:
            raise ValueError("Prompt is required")

        v = Video(prompt=prompt)

        title = self._make_title(v)
        script = self._make_script(v, title)
        summary = self._make_summary(v, script)

        url, duration = self._upload_rendered(script)

        v = replace(
            v,
            title=title,
            script=script,
            summary=summary,
            url=url,
            duration=duration,
            views=0,
        )

        self.repo.save(v)
        return v

    def _make_title(self, v: Video) -> str:
        if not v.prompt:
            raise RuntimeError("Prompt not set, can't fill title")
        return "Example Title"

    def _make_script(self, v: Video, title: str) -> str:
        if not title:
            raise RuntimeError("Title not set, can't fill title")
        return "Example"

    def _make_summary(self, v: Video, script: str) -> str:
        if not script:
            raise RuntimeError("Script not set, can't fill title")
        return "Example"

    def _upload_rendered(self, script: str) -> Tuple[str, float]:
        """
        Uploads video to bucket and returns url, duration
        :return: url for video
        """
        return "https://", 1.1
