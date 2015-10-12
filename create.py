import sqlite3 
import csv

conn = sqlite3.connect("blog.db")
c = conn.cursor()

q = "CREATE TABLE users(username text, password text)"
c.execute(q)

q = "CREATE TABLE posts(id int, username text, title text, post text)"
c.execute(q)

q = "CREATE TABLE comments(id int, username text, comment text)"

conn.commit()

