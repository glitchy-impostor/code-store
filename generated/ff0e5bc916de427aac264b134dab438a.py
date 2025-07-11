
from flask import Flask, jsonify

app = Flask(__name__)

# Define a sample API endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    """Return a simple greeting."""
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    # Driver function to run the Flask application
    app.run(host='localhost', port=8080)
