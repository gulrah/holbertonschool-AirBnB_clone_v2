#!/usr/bin/python3
"""
Start a Flask web app
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Route to display cities grouped by states
    """
    obj = storage.all('State')
    states_list = []
    for k, v in obj.items():
        states_list.append(v)
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
