from flask import Flask, render_template,request, session,redirect, url_for
import sqlite3
import csv

app= Flask(__name__)
loggedin= False

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
        if uname=="this" and pword=="that":
            loggedin= True
            return redirect(url_for('profile'))
        else:
            return(render_template("login.html") + uname + "<br>" +pword)
            #print (uname + password)

@app.route("/profile")
def profile():
    return "shhs"
    
if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)
