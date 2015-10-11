import sqlite3 
import csv

#Need to make the database name, fill it in for the empty strings
connect = sqlite3.connect("blog.db")
c = connect.cursor()

q = "create table users (username text, password text)"
c.execute(q)

connect.commit()

