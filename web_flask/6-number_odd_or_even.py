#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display 'C' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """display 'Python ', followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """display 'n is a number' only if n is an integer"""
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evens = 'even'
    else:
        evens = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evens=evens)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
