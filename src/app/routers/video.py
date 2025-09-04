from flask import Blueprint


video = Blueprint("video", __name__)


@video.route("/create_video", methods=["POST"])
def create_video_handler():
    pass
