#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Print 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Print 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Print 'C ' followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Print 'Python ' followed by the value of the text variable."""
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
