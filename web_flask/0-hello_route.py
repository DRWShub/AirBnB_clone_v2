#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)


from flask import Flask, request
from flask_restful import Resource, Api
import sys
import os

app = Flask(__name__)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

class topic_tags(Resource):
    def get(self):
        return {'Hello HBNB!'}

api.add_resource(topic_tags, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
