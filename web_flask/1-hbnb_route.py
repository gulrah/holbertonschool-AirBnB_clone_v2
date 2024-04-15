#!/usr/bin/python3
"""Start a Flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route displays 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
