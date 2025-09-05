from typing import Protocol, Optional

from src.app.domain.llm import Tool


class LLMClient(Protocol):
    def call_llm(
        self,
        prompt: str,
        model: str = "gpt-5-mini",
        system: str = "You are a helpful assistant",
        effort: Optional[str] = None,
        tools: Optional[Tool] = None,
    ) -> str: ...
