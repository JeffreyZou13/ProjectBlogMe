from flask import Flask, render_template,request, session,redirect, url_for
import sqlite3
import csv
import utils

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
        if utils.authenticate(uname,pword): # checks if pword matches uname in database
            loggedin= True
            return redirect(url_for('profile'))
        else:
            return(render_template("login.html") + uname + "<br>" +pword)
            #print (uname + password)

@app.route("/logout") # redirects to login page
def logout():
	return redirect(url_for("login"))

@app.route("/profile")
def profile():
	if loggedin:
		return(render_template("profile.html"))
	else:
		return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)
