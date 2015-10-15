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
@app.route("/login/<message>", methods=["GET","POST"])
def login(message=''):
    if request.method== "GET":
        return(render_template("login.html",message=message))
    else:
        uname=request.form['username']
        pword = request.form['password']
        if utils.authenticate(uname,pword): # checks if pword matches uname in database
            #loggedin= True
	    session['user'] = uname # set current user 
            return redirect(url_for('profile', username=uname))
        else:
            return(render_template("login.html",message="Incorrect username or password.") +uname+ "<br>" +pword)
    		# return login.html with error message

@app.route("/logout") # redirects to login page
def logout():
	session['user'] = ''
	return redirect(url_for("login"))

@app.route("/profile")
@app.route("/profile/<username>")
def profile(username="Default"):
	post_list = utils.posts(username)
	return(render_template("profile.html",username=username,post_list=post_list))
    
@app.route("/post", methods=["GET","POST"])
@app.route("/post/<post_id>", methods=["GET","POST"])
def post(post_id="1"):
	if request.method == "POST":
		if 'user' in session and session['user'] != '':
			comment = request.form['comment']
			print comment
			# add comment to database
		else:
			return redirect(url_for("login",message="Login before you post."))
	d = utils.post_info(post_id)
	comment_list = utils.comments(post_id)
	return(render_template("post.html",d=d,comment_list=comment_list))

@app.route("/newpost", methods=["GET","POST"])
def newpost():
	if request.method == "GET":
		if 'user' in session and session['user'] != '':
			return(render_template("newpost.html"))
		else:
			return redirect(url_for("login",message="Login before you post."))
	else:
		title = request.form['title']
		post = request.form['post']
		# add post to database
		return redirect(url_for("post",post_id=1)) # redirect to new post

if __name__ == "__main__":
    app.debug=True
    app.secret_key = "allha1lthemajest1cplatyp1"
    app.run(host="0.0.0.0",port=5000)
