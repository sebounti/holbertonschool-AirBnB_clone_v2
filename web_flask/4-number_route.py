#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    result = text.replace('_', ' ')
    return 'C {}'.format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text='is cool'):
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
