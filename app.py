from flask import Flask, render_template,request, session,redirect, url_for
import sqlite3
import csv
import utils

app= Flask(__name__)

@app.route("/")
def default():
    return redirect (url_for('home'))

@app.route("/home")
def home():
    return(render_template("home.html"))

@app.route("/login", methods=["GET","POST"])
@app.route("/login/<message>", methods=["GET","POST"])
def login(message='',logout=False):
    if request.method== "GET":
	    if 'user' in session and session['user'] != '':
		return(render_template("login.html",message='Already logged in.',logout=True))
	    else:
        	return(render_template("login.html",message=message))
    else:
        uname=request.form['username']
        pword = request.form['password']
	if not utils.user_exists(uname):
		return(render_template("login.html",message="User does not exist."))
        elif utils.authenticate(uname,pword): # checks if pword matches uname in database
	    session['user'] = uname # set current user 
            return redirect(url_for('profile', username=uname))
        else:
            return(render_template("login.html",message="Incorrect username or password."))

@app.route("/register", methods=["GET","POST"])
@app.route("/register/<message>", methods=["GET","POST"])
def register():
	if request.method == "GET":
		return(render_template("register.html"))
	else:
		uname = request.form['username']
		pword = request.form['password']
		conf = request.form['confirm']
		if utils.user_exists(uname):
			return(render_template("register.html",message="Username already exists."))
		elif len(uname) < 2:
			return(render_template("register.html",message="Username must be at least 2 characters."))
		elif len(pword) < 6:
			return(render_template("register.html",message="Password must be at least 6 characters."))
		elif pword != conf:
			return(render_template("register.html",message="Password doesn't match confirmation."))
		else:
			utils.add_user(uname,pword)
			return redirect(url_for('login'))
	#form input for post

@app.route("/logout") # redirects to login page
def logout():
	#session['user'] = ''
	session.clear()
	return redirect(url_for("login"))

@app.route("/profile")
@app.route("/profile/<username>")
def profile(username="Default"):
	post_list = utils.posts(username)
	return(render_template("profile.html",username=username,post_list=post_list))

@app.route("/myprofile")
def myprofile():
	if 'user' in session and session['user'] != '':
		return redirect(url_for("profile",username=session['user']))
	else:
		return redirect(url_for("login",message="Login to see your profile."))

    
@app.route("/post", methods=["GET","POST"])
@app.route("/post/<post_id>", methods=["GET","POST"])
def post(post_id="1"):
	if request.method == "POST":
		if 'user' in session and session['user'] != '':
			comment = request.form['comment']
			# add comment to database
			utils.add_comment(post_id,session['user'],comment)
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
		utils.add_post(session['user'],title,post)
		return redirect(url_for("post",post_id=1)) # redirect to new post

@app.route("/posts", methods=["GET","POST"])
def delete(post_id="None"):
    #username and password of the current user
    uname = request.form['username']
    pword = request.form['password']
    #compares the person who posts to the person trying to delete
    if check_name(post_id) == uname:
        utils.delete_post(post_id)
        return render_template("/profile/<username>")

if __name__ == "__main__":
    app.debug=True
    app.secret_key = "allha1lthemajest1cplatyp1"
    app.run(host="0.0.0.0",port=5000)
