#!/usr/bin/python3
"""
    Starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Returns a Hello"""
    return "Hello HBNB"

@pp.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run()
