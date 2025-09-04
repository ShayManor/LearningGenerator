from flask import Blueprint, request, jsonify, Response

from src.app.gateways.llm.clients.openai_client import OpenAIClient
from src.app.gateways.llm.llm_client import LLMClient
from src.app.gateways.storage.clients.S3_storage import S3Storage
from src.app.gateways.storage.storage import Storage
from src.app.repositories.db import session_factory
from src.app.repositories.sqlalchemy_video_repo import SqlAlchemyVideoRepo
from src.app.repositories.video_repo import VideoRepo
from src.services.create_video import CreateVideoService

video = Blueprint("video", __name__)


@video.route("/create_video", methods=["POST"])
def create_video_handler() -> Response:
    data: dict = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing 'prompt' in JSON"})

    s3_storage: Storage = S3Storage("example_bucket")
    openai_client: LLMClient = OpenAIClient()
    video_repo: VideoRepo = SqlAlchemyVideoRepo(session_factory)
    video_service = CreateVideoService(video_repo, openai_client, s3_storage)
    video_service.execute(prompt=prompt)
    return jsonify({"success": True}, 200)
