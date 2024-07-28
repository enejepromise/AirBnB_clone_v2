#!/usr/bin/python3
"""
    A script that starts a Flask web application
"""
from flask import Flask
app = (__name__)

@app.routes("/", strict_slashes=False)
def hello():
    """Return hello"""
    return "Hello HBNB"

@pp.routes("/hbnb", strict_slashes=False)
def hbnb():
    """Returns hbnb"""
    return "HBNB"

If __name__ == "__main__":
    app.run()
