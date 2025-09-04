from typing import Protocol


class LLMClient(Protocol):
    def ping(self, prompt: str) -> str: ...
