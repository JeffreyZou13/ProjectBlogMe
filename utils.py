import csv
import sqlite3

def authenticate(uname, pword):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT password
	FROM users
	WHERE username=?'''
	result = c.execute(q, (uname,))
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
	WHERE username=?'''
	result = c.execute(q, (uname,))
	posts = []
	for r in result:
		h = "http://localhost:5000/post/"+str(r[0])
		posts += [{'id':h,'title':r[2]}]
	return posts

def post_info(post_id):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = '''
	SELECT * 
	FROM posts
	WHERE id=?'''
	result = c.execute(q,(post_id,))
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
	WHERE id=?'''
	result = c.execute(q, (str(post_id),))
	comments = []
	for r in result:
		comments += [{'user':r[1],'comment':r[2]}]
	return comments

def user_exists(name):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = 'SELECT * FROM users WHERE username="'+name+'"'
	result = c.execute(q)
	num = 0
	for r in result:
		num = num + 1
	if num != 0:
		return True
	else:
		return False

def add_user(name,password):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = 'INSERT INTO users VALUES("'+'","'.join([name,password])+'")'
	print q
	c.execute(q)
	conn.commit()

def add_post(user,title,post):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = 'SELECT COUNT(*) FROM posts'
	result = c.execute(q) # number of posts
	for r in result:
		pid = r[0]+1
	q = 'INSERT INTO posts VALUES("'+'","'.join([str(pid),user,title,post])+'")'
	print q
	c.execute(q)
	'''
	c.execute(".mode csv")
	c.execute(".output posts.csv")
	c.execute("SELECT * FROM posts")
	c.execute(".output stdout")
	'''
	conn.commit()

def add_comment(pid,user,comment):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	q = 'INSERT INTO comments VALUES("'+'","'.join([pid,user,comment])+'")'
	c.execute(q)
	conn.commit()
