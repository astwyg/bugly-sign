# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import urllib2,urllib
import cookielib
import json, datetime
from signOnce import signOnce

import sys
reload(sys)
sys. setdefaultencoding('utf8')

import logging
LOG_FILENAME="log.txt"
logging.basicConfig(filename=LOG_FILENAME,level=logging.WARNING)

app = Flask(__name__, static_folder='front')

@app.route('/')
def index():
    return render_template('index.html', debugMode=False)

@app.route('/api/sign',  methods=['POST'])
def sign():
    form = request.get_json()
    result = signOnce(form["iccid"],form["phone"],form["password"])
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")
