import csv
import sqlite3

def authenticate(uname, pword):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT password
	FROM users
	WHERE username="'''+uname+'"'
	result = c.execute(q)
	for r in result:
		p = r[0]
	if p == pword:
		return True
	else:
		return False

def posts(uname):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT *
	FROM posts
	WHERE username="'''+uname+'"'
	result = c.execute(q)
	posts = []
	for r in result:
		h = "http://localhost:5000/post/"+str(r[0])
		posts += [[h,r[2]]]
	return posts

def post_info(post_id):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT * 
	FROM posts
	WHERE id='''+post_id
	result = c.execute(q)
	d = {}
	for r in result:
		d['user'] = r[1]
		d['title'] = r[2]
		d['post'] = r[3]
	return d

def comments(post_id):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT *
	FROM comments
	WHERE id="'''+str(post_id)+'"'
	result = c.execute(q)
	comments = []
	for r in result:
		comments += [[r[1],r[2]]]
	return comments

#print comments(1)
