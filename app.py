from flask import Flask, render_template,request, session,redirect, url_for
import sqlite3
import csv
import utils

app= Flask(__name__)
#loggedin= False

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
            #loggedin= True
            return redirect(url_for('profile', username=uname))
        else:
            return(render_template("login.html") +uname+ "<br>" +pword)
    		# return login.html with error message

@app.route("/logout") # redirects to login page
def logout():
	return redirect(url_for("login"))

@app.route("/profile")
@app.route("/profile/<username>")
def profile(username="Default"):
	post_list = utils.posts(username)
	return(render_template("profile.html",username=username,post_list=post_list))
    
@app.route("/post")
@app.route("/post/<post_id>")
def post(post_id="1"):
	d = utils.post_info(post_id)
	comment_list = utils.comments(post_id)
	return(render_template("post.html",d=d,comment_list=comment_list))

@app.route("/newpost")
def newpost():
	return(render_template("newpost.html"))

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
