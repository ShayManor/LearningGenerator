from dataclasses import dataclass


@dataclass
class Tool:
    WEB_SEARCH: bool = False
    X_MCP: bool = False
    CODE_INTERPRETER: bool = False
    GENERATE_IMAGE: bool = False
