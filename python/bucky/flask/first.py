#!/usr/bin/python
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Method used: %s" % request.method


@app.route('/profile/<username>')
def profile(username):
    return '<h2>Tuna is good, right %s ? \n Damn right!</h>' % username

if __name__ == "__main__":
    app.run(debug=True)
