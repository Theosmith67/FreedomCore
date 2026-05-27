from flask import Flask, jsonify
from sys import path
from os.path import dirname, abspath

# Add parent directory to path to import from 03_routes
path.insert(0, dirname(dirname(abspath(__file__))))

# Import the routes blueprint
from routes.routes import routes_bp

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)
