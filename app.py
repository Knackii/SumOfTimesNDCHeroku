# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:33:16 2021

@author: Flirno
"""

import api
from flask import Flask, render_template
import json 
from datetime import date  
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

today = str(date.today())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@app.route("/")
@app.route("/home")
@app.route("/index")
def hello():
    return ('<!DOCTYPE html><html><head><title>NDC - Edition 1 updater</title></head><body><h1>update every hours</h1></body></html>')



#---------------------PUBLIC-----------------------#

@app.route('/update')
def update():
    api.update
    return("good")


    
if __name__ == "__main__":
    app.run(debug=True)
