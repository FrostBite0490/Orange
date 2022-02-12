
from crypt import methods
from dis import dis
from re import T
from unicodedata import name
from unittest import expectedFailure, result
import mariadb
from flask import Flask,render_template,request
from markupsafe import re
#from forms import UserForm
import os
import csv
import pandas as pd
#from sqlalchemy import false, null, true
import sys
import sort

SECRET_KEY = os.urandom(32)
global sup

try:
    conn=mariadb.connect(
        user="kamal",
        password="k1",
        host='localhost',
        database='orange'
    )
except mariadb.Error as e:
    print(e)
    sys.exit(1) 
    
def read_maria():    
    phonelist=[]
    cur = conn.cursor()
    cur.execute("SELECT* FROM phonelist")
    for(name,performance,display,battery,camera,price) in cur:
        phonedata={
            'gaming':performance.__float__(),
            'batt':battery.__float__(),
            'disp':display.__float__(),
            'cam':camera.__float__(),
            'name':name.__str__(),
            'price':price.__float__()}
        #print(phonedata)
        phonelist.append(phonedata)
    #print(phonelist)
    sort.analyze(phonelist)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def hello_world():
    data='a'
    return render_template('Rating.html',data=data)
    
@app.route('/2',methods=['POST','GET'])
def r2():
    if request.method=='POST':
        #val=request.form.get("1")
        #print(val)
        return render_template("Rating2.html")    

#read_maria()
if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0')
