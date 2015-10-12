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
