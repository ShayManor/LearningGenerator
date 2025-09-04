from typing import Optional

from src.app.gateways.llm.llm_client import LLMClient


class OpenAIClient(LLMClient):
    def __init__(self) -> None:
        pass

    def call_llm(
        self,
        prompt: str,
        model: str = "gpt-5-mini",
        effort: Optional[str] = None,
        tools: Optional[dict] = None,
    ) -> str:
        return "Example Response"
