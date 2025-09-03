from flask import send_file
import importlib.resources as r

from flask import Blueprint

STATIC_DIR = r.files("src").joinpath("static")
static = Blueprint("static", __name__)


@static.route("/", methods=["GET"])
def root():
    return send_file(str(STATIC_DIR / "index.html"))


@static.route("/<page>", methods=["GET"])
def any_page(page):
    return send_file(str(STATIC_DIR / page))
