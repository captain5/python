#!/bin/env python
# _*_coding:utf-8_*_
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Please input url like this:\n<br>http://ubuntucd/12594</h1> SN:12594 <form><'

@app.route('/<path:sn>')
def sayHello(sn):
    print sn
    sn0 = './mk -s ' + sn
    output = os.popen(sn0)
    return '<h1> SN:\n %s </h1>' % output.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
