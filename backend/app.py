from flask import Flask, jsonify
from flask_cors import CORS
from routes import app as routes_app
import requests

app = Flask(__name__)
CORS(app)

url = 'http://localhost:5000/exercises'

# Обработчик для корневого URL
@app.route('/')
def hello():
    return jsonify(message="Hello, World!")


if __name__ == '__main__':
    app.register_blueprint(routes_app)
    app.run(debug=True)
