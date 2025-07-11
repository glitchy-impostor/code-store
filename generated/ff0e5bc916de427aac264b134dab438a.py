
from flask import Flask, jsonify
import random
import string

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

# Define an API endpoint to generate a random number
@app.route('/api/random_number', methods=['GET'])
def random_number():
    """Return a random number between 1 and 100."""
    return jsonify(number=random.randint(1, 100))

# Define an API endpoint that returns a random response from an array of predefined responses
@app.route('/api/random_response', methods=['GET'])
def random_response():
    """Return a random response from an array of predefined responses."""
    responses = [
        "Response 1", "Response 2", "Response 3", "Response 4", "Response 5",
        "Response 6", "Response 7", "Response 8", "Response 9", "Response 10",
        "Response 11", "Response 12", "Response 13", "Response 14", "Response 15",
        "Response 16", "Response 17", "Response 18", "Response 19", "Response 20",
        "Response 21", "Response 22", "Response 23", "Response 24", "Response 25",
        "Response 26", "Response 27", "Response 28", "Response 29", "Response 30",
        "Response 31", "Response 32", "Response 33", "Response 34", "Response 35",
        "Response 36", "Response 37", "Response 38", "Response 39", "Response 40",
        "Response 41", "Response 42", "Response 43", "Response 44", "Response 45",
        "Response 46", "Response 47", "Response 48", "Response 49", "Response 50"
    ]
    return jsonify(response=random.choice(responses))

# Define an API endpoint that returns the Caesar shifted code of a message
@app.route('/api/caesar_shift/<string:message>/<int:shift>', methods=['GET'])
def caesar_shift(message, shift):
    """Return the Caesar shifted code of a message."""
    shifted_message = ''.join([chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else char for char in message])
    return jsonify(shifted_message=shifted_message)

def run_app():
    app.run(port=1000)

if __name__ == '__main__':
    # Driver function to run the Flask application
    run_app()
