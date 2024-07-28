#!/usr/bin/python3

"""
Starts a Flask web application:
"""

from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello():

    """Returns a Hello"""
    return "Hello HBNB"

@app.route("/hbnb", strict_slashes=False)
def hbnb():

    """Returns a HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Return C text value"""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run
