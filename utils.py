import csv
import sqlite3

conn = sqlite3.connect("blog.db")
c = conn.cursor()

def authenticate(uname, pword):
	q = '''
	SELECT users.password
	FROM users
	WHERE users.username='''+uname
	result = c.execute(q)
	if result == pword:
		return True
	else:
		return False
