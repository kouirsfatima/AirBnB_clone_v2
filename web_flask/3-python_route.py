#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """print HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """print HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text (text):
    """print C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))
@app.route('/python/<text>')
def python_text(text):
    """print puthon followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
