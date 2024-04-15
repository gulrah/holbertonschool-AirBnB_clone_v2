#!/usr/bin/python3
"""
Start a Flask web app
"""

from flask import Flask
from markupsafe import escape

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
    return "C {}".format(escape(text).replace('_', ' '))


@app.errorhandler(404)
def page_not_found(error):
    """
    Handler for 404 errors
    """
    return "Not found", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
