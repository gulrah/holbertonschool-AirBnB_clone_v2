#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with states and their cities"""
    states = storage.all(State).values()
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        states = sorted(states, key=lambda state: state.name)
    else:
        states = sorted(states, key=lambda state: state.name.lower())
        
        return render_template('8-cities_by_states.html', states=states)
                            
    
@app.teardown_appcontext
def teardown_db(exception):
"""Remove the current SQLAlchemy session"""
storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
