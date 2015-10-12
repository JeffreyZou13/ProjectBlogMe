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
		posts += [r[0]]
	return posts

def comments(post_id):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT *
	FROM comments
	WHERE username="'''+uname+'"'
	result = c.execute(q)
	comments = []
	for r in result:
		comments += [r[0]]
	return comments
