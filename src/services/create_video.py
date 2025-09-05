from dataclasses import replace
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

    def execute(self, prompt: str) -> Video:
        if not prompt:
            raise ValueError("Prompt is required")

        v = Video(prompt=prompt)

        v.title = self._make_title(v)
        v.desc = self._make_description(v)
        v.script = self._make_script(v)
        v.summary = self._make_summary(v)

        v.url, v.duration = self._upload_rendered(v)

        v = replace(
            v,
            views=0,
        )

        self.repo.save(v)
        return v

    def _make_title(self, v: Video) -> str:
        if not v.prompt:
            raise RuntimeError("Prompt not set, can't fill title")
        title = self.llm.call_llm(
            prompt=v.prompt,
            model="gpt-4.1-mini-2025-04-14",
            system="create_video_title",
        )
        return title

    def _make_description(self, v: Video) -> str:
        if not v.prompt:
            raise RuntimeError("Prompt not set, can't fill description")
        if not v.title:
            raise RuntimeError("Title not set, can't fill description")
        desc = self.llm.call_llm(
            prompt=f"Prompt: {v.prompt}\n\nTitle: {v.title}",
            model="gpt-5-mini",
            system="create_video_desc",
        )
        print(desc)
        return desc

    def _make_script(self, v: Video) -> str:
        if not v.title:
            raise RuntimeError("Title not set, can't fill title")
        if not v.description:
            raise RuntimeError("Description not set, can't fill title")
        if not v.prompt:
            raise RuntimeError("Prompt not set, can't fill title")

        web_tool = Tool()
        web_tool.WEB_SEARCH = True
        script = self.llm.call_llm(
            prompt=f"Prompt: {v.prompt}\n\nTitle: {v.title}\n\nDescription: {v.description}",
            model="gpt-5",
            system="create_video_script",
            tools=web_tool,
        )
        return script

    def _make_summary(self, v: Video) -> str:
        if not v.script:
            raise RuntimeError("Script not set, can't fill title")
        return "Example"

    def _upload_rendered(self, v) -> Tuple[str, float]:
        """
        Uploads video to bucket and returns url, duration
        :return: url for video
        """
        return "https://", 1.1
