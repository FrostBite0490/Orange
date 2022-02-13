
from crypt import methods
from dis import dis
from re import T
from unicodedata import name
from unittest import expectedFailure, result
import mariadb
from flask import Flask,render_template, render_template_string,request
from markupsafe import re
#from forms import UserForm
import os
import csv
import pandas as pd
#from sqlalchemy import false, null, true
import sys
import sort

SECRET_KEY = os.urandom(32)
gaming,batt,disp,cam,price=0,0,0,0,0

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
        phonelist.append(phonedata)
        #print(phonedata)
    #print(phonelist)        
    return phonelist
    
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def hello_world():
    data='a'
    return render_template('Rating.html',data=data)
    
@app.route('/2',methods=['POST','GET'])
def r2():
   
    #if(request.form['rating']):
    gaming=float(request.form['rating'])
    if gaming!=0:
        return render_template("Rating2.html")
    else:
        print('Noooooo')
        return render_template("Rating.html",q='Gaming',data="Select A Value")
@app.route('/3',methods=['POST','GET'])
def r3():
    if request.method=='POST':
        global batt
        batt=float(request.form['rating'])
        if batt!=0:
            print("-------",batt)
            return render_template("Rating3.html") 
        else:
            return render_template("Rating2.html",data="Select")
@app.route('/4',methods=['POST','GET'])
def r4():
    if request.method=='POST':
        global disp
        disp=float(request.form['rating'])
        if disp!=0:
            print("-------",disp)
            return render_template("Rating4.html") 
        else:
            return render_template("Rating3.html",data="Select")

@app.route('/5',methods=['POST','GET'])
def r5():
    if request.method=='POST':
        global cam
        cam=float(request.form['rating'])
        if cam!=0:
            print("-------",cam)
            return render_template("Rating5.html") 
        else:
            return render_template("Rating4.html",data="select")

@app.route('/f',methods=['POST','GET'])
def final():
    if request.method=='POST':
        global gaming,batt,disp,cam
        price=float(request.form['rating'])
        if price!=0:
            print("-------",price)
            phonelist=read_maria()
            user_pref={
                'gaming':gaming,
                'batt':batt,
                'disp':disp,
                'cam':cam,
                'price':price,
                'name':''}
            phone=sort.analyze(phonelist,user_pref)
            print(phonelist)
            return render_template("final.html",data=phone) 
        else:
            return render_template("Rating5.html",data="Select")
        
print(cam) 
#read_maria()
if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0')
