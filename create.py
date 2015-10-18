import sqlite3 
import csv

conn = sqlite3.connect("blog.db")
c = conn.cursor()

q = "CREATE TABLE users(username text, password text, email text)"
c.execute(q)

q = "CREATE TABLE posts(id int, username text, title text, post text, date text, time text)"
c.execute(q)

q = "CREATE TABLE comments(id int, username text, comment text, date text, time text)"
c.execute(q)

conn.commit()

