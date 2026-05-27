from flask import Blueprint, render_template, request, jsonify

# Import your core orchestration module
from freedom_core.core import generate_response

# Define your route blueprint
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def index():
    # Renders your main user interface layout
    return render_template('index.html')

@routes_bp.route('/bot', methods=['POST'])
def bot_response():
    # 1. Grab the raw incoming JSON payload from your HTML form
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        # 2. Pass the message directly into freedom_core to analyze mood,
        #    apply persona weights, log to memory, and get a tailored response.
        ai_reply = generate_response(user_message)
        
        # 3. Hand the real AI output back to your frontend HTML interface
        return jsonify({"response": ai_reply})
        
    except Exception as e:
        return jsonify({"response": f"Core Error: {str(e)}"}), 500