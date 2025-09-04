from flask import jsonify, Blueprint, Response

health = Blueprint("health", __name__)


@health.route("/health", methods=["GET"])
def health_check() -> Response:
    return jsonify({"ping": "pong"})


@health.route("/health/<data>", methods=["GET"])
def health_data(data: str) -> Response:
    return jsonify({"given": data})
