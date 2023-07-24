#!/usr/bin/python3
"""Script starts a Flask web application"""
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    name = request.args.get("name", "HBNB")
    return f'Hello {escape(name)}!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
