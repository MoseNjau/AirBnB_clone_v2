#!/usr/bin/python3
"""Flask app initialization"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns a string at the /hbnb_filters route"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
