#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>')
def number_n(n):
    """n is a number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
