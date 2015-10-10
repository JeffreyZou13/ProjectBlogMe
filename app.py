from flask import Flask, render_template,request
from flask import redirect, url_for
import sqlite3
import csv

app= Flask(__name__)

@app.route("/")
def default():
    return redirect (url_for('home'))

@app.route("/home")
def home():
    return(render_template("home.html"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method== "GET":
        return(render_template("login.html"))
    else:
        uname=request.form['username']
        pword = request.form['password']
        #button= request.form['button']
        if uname=="this" and pword=="that":
            return "<h1>yey</h1> <hr>" +uname +pword
        else:
            return(render_template("login.html") + uname + "<br>" +pword)
            #print (uname + password)"""
    

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)
