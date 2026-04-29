from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.sanitizer import sanitize_input

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Get request data
        data = request.get_json()

        # Validate request body
        if not data or "input" not in data:
            return jsonify({
                "status": "error",
                "message": "Input field is required"
            }), 400

        user_input = data["input"]

        # Validate input type
        if not isinstance(user_input, str) or not user_input.strip():
            return jsonify({
                "status": "error",
                "message": "Invalid input"
            }), 400

        # Sanitize input
        clean_input = sanitize_input(user_input)

        # Detect unsafe / prompt injection
        if not clean_input:
            return jsonify({
                "status": "error",
                "message": "Unsafe input detected"
            }), 400

        # Call Groq AI
        result = call_groq(clean_input)

        # Success response
        return jsonify({
            "status": "success",
            "input": clean_input,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500