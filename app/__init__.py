from flask import Flask, jsonify
from flask_cors import CORS

from app.database import init_db
from app.routes import api_bp, pages_bp


def create_app():
    app = Flask(__name__)

    CORS(app)

    init_db()

    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)

    @app.route("/health")
    def health():
        return jsonify({
            "success": True,
            "status": "active"
        })

    return app