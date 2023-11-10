from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the AI Bank Project API!"})

@app.route('/test')
def test():
    return jsonify({"message": "Test successful!"})


if __name__ == '__main__':
    app.run(debug=True)
