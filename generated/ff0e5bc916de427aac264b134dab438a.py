
from flask import Flask, jsonify

app = Flask(__name__)

# Define sample API endpoint for "Hello, world!"
@app.route('/api/hello', methods=['GET'])
def hello():
    """Return a simple greeting."""
    return jsonify(message="Hello, world!")

# Define another API endpoint that returns a different message
@app.route('/api/goodbye', methods=['GET'])
def goodbye():
    """Return a different greeting."""
    return jsonify(message="Goodbye, world!")

# Define an API endpoint that echoes back the user's input
@app.route('/api/echo/<string:message>', methods=['GET'])
def echo(message):
    """Echo back the user's input."""
    return jsonify(message=message)

if __name__ == '__main__':
    # Driver function to run the Flask application
    app.run(host='localhost', port=8080)
