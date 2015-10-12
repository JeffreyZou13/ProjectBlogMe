import sqlite3 
import csv

#Need to make the database name, fill it in for the empty strings
conn = sqlite3.connect("blog.db")
c = conn.cursor()

q = "CREATE TABLE users(username text, password text)"
c.execute(q)

conn.commit()

