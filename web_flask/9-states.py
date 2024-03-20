#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Function that returns Hello HBNB! """
    return render_template('9-states.html', states=storage.all("State"))


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Function that returns Hello HBNB! """
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
