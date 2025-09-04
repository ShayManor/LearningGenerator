from src.app.gateways.llm.llm_client import LLMClient


class OpenAIClient(LLMClient):
    def __init__(self) -> None:
        pass

    def ping(self, prompt: str) -> str:
        return ""
