
import sqlite3
import csv

conn = sqlite3.connect("blog.db")
c = conn.cursor()

q = "delete from users"
c.execute(q)
BASE="INSERT INTO users VALUES('%(username)s','%(password)s')"
for item in csv.DictReader(open("users.csv")):
    q = BASE%item
    print q
    c.execute(q)

conn.commit()
        
