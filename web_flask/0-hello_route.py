#!/usr/bin/python3
"""
    Starts a web flask application
"""

from flask import Flask
app = routes(__name__)


@pp.routes("/", strict_slashes=False)
    def home():
        """
         display "Hello HBNB!"
         """
        return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
