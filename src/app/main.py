import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from src.app.routers.health import health
from src.app.routers.static import static
from src.app.routers.db import db
from src.app.routers.video import video


load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(health)
    app.register_blueprint(static)
    app.register_blueprint(db)
    app.register_blueprint(video)
    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)), debug=True)
