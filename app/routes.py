from flask import Blueprint, jsonify, render_template, request

from app.database import add_lead, get_all_leads
from app.services.ai_service import ai_service, AIServiceError


pages_bp = Blueprint("pages", __name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")


@pages_bp.route("/")
def index():
    return render_template("index.html")


@pages_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    try:
        data = request.get_json(silent=True) or {}
        message = data.get("message", "").strip()
        history = data.get("history", [])

        if not message:
            return jsonify({
                "success": False,
                "error": "Mesaj alanı boş bırakılamaz."
            }), 400

        answer = ai_service.yanit_uret(message, history)

        return jsonify({
            "success": True,
            "answer": answer
        })

    except AIServiceError as error:
        
        return jsonify({
            "success": False,
            "error": "Yapay zekâ servisine şu anda ulaşılamıyor."
        }), 503


@api_bp.route("/leads", methods=["POST"])
def create_lead():
    try:
        data = request.get_json(silent=True) or {}

        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        email = data.get("email", "").strip()
        message = data.get("message", "").strip()

        if not name or not phone:
            return jsonify({
                "success": False,
                "error": "İsim ve telefon alanları zorunludur."
            }), 400

        add_lead(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        return jsonify({
            "success": True,
            "message": "Müşteri adayı başarıyla kaydedildi."
        }), 201

    except Exception:
        return jsonify({
            "success": False,
            "error": "Müşteri kaydı oluşturulamadı."
        }), 500


@api_bp.route("/leads", methods=["GET"])
def list_leads():
    try:
        leads = get_all_leads()

        return jsonify({
            "success": True,
            "leads": leads
        })

    except Exception:
        return jsonify({
            "success": False,
            "error": "Müşteri kayıtları alınamadı."
        }), 500