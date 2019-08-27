import json
import os
from flask import Flask, abort, render_template, request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        html = render_template('index.html', data={})
    html = render_template('index.html', data={})
    return html


@app.route('/hoge', methods=['POST', 'GET'])
def hoge():
    return


@app.route("/test", methods=['POST', 'GET'])
def fuga():
    return


if __name__ == "__main__":
    app.run()
