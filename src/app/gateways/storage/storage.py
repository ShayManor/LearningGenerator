from typing import Protocol, BinaryIO


class Storage(Protocol):
    def upload(self, file: BinaryIO, key: str, content_type: str) -> str:
        """Upload file-like object, return public URL"""
        ...

    def delete(self, key: str) -> None:
        """Remove file from storage"""
        ...
