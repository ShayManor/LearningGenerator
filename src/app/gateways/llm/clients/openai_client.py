import json
import os
from pathlib import Path
from typing import Optional, cast, List

from openai import OpenAI, NOT_GIVEN
from openai.types.responses import ToolParam
from openai.types.shared_params.reasoning import Reasoning

from src.app.domain.llm import Tool
from src.app.gateways.llm.llm_client import LLMClient


def get_tools(tool: Tool) -> List[ToolParam]:
    openai_tools: List[ToolParam] = []
    if tool.X_MCP:
        openai_tools.append(
            cast(
                ToolParam,
                {
                    "type": "mcp",
                    "server_label": "dmcp",
                    "server_description": "A GPU Finder MCP ",
                    "server_url": "https://gpufindr.com/mcp/sse",
                    "require_approval": "never",
                },
            )
        )

    if tool.WEB_SEARCH:
        openai_tools.append(cast(ToolParam, {"type": "web_search"}))
    if tool.GENERATE_IMAGE:
        openai_tools.append(cast(ToolParam, {"type": "image_generation"}))

    if tool.CODE_INTERPRETER:
        openai_tools.append(
            cast(ToolParam, {"type": "code_interpreter", "container": {"type": "auto"}})
        )
    return openai_tools


class OpenAIClient(LLMClient):
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("No OPENAI_API_KEY set.")
        self.client = OpenAI(api_key=api_key)
        self.system_prompts: dict = {}
        system_path = Path(__file__).resolve().parent.parent
        with open(system_path / "prompts.json", "r") as f:
            self.system_prompts = json.load(f)

    def clean_result(self, prompt: str) -> str:
        return prompt

    def call_llm(
        self,
        prompt: str,
        model: str = "gpt-5-mini",
        system: str = "You are a helpful assistant",
        effort: Optional[str] = None,
        tools: Optional[Tool] = None,
    ) -> str:
        from openai import NotGiven

        reasoning: Reasoning | NotGiven = (
            cast(Reasoning, {"effort": effort})  # effort is not None here
            if effort is not None
            else NOT_GIVEN
        )
        response = self.client.responses.create(
            input=prompt,
            model=model,
            instructions=self.system_prompts[system],
            reasoning=reasoning,
            tools=get_tools(tools) if tools else NOT_GIVEN,
        )
        return response.output_text
