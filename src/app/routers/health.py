from flask import jsonify, Blueprint

health = Blueprint("health", __name__)


@health.route("/health", methods=["GET"])
def health_check():
    return jsonify({"ping": "pong"})


@health.route("/health/<data>", methods=["GET"])
def health_data(data):
    return jsonify({"given": data})
