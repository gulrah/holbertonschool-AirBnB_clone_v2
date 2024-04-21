#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of all State objects"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def cities_by_state(state_id):
    """Display a HTML page with a list of City objects
    linked to the State specified by state_id"""
    state = storage.get(State, state_id)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
