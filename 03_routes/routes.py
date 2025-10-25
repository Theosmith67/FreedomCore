from flask import Blueprint, render_template, request, jsonify
# Create a Blueprint instance
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')  # or whatever your homepage is

@main.route('/bot', methods=['POST'])
def bot():
    user_input = request.json.get("message")
    
    # Dummy response for now — replace with actual model call later
    response =f"Echo:{user_input}"
    
    return jsonify({"response": response})

