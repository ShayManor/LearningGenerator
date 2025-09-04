from typing import Protocol, Optional


class LLMClient(Protocol):
    def call_llm(
        self,
        prompt: str,
        model: str = "gpt-5-mini",
        effort: Optional[str] = None,
        tools: Optional[dict] = None,
    ) -> str: ...
