#!/usr/bin/python3
"""
Start a Flask web app
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route displays 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """
    Route displays 'C ' followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Route displays 'Python ' followed by the value of the text variable
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route displays 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)


@app.errorhandler(404)
def page_not_found(error):
    """
    Handler for 404 errors
    """
    return "Not found", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
