import sqlite3
import csv

conn = sqlite3.connect("blog.db")
c = conn.cursor()

q = "delete from users"
c.execute(q)
BASE="INSERT INTO users VALUES(%s,%s)"
for item in csv.DictReader(open("users.csv")):
    q = BASE%item
    print q
    c.execute(q, (username, password))

q = "delete from posts"
c.execute(q)
BASE="INSERT INTO posts VALUES(%s,%s,%s,%s)"
for item in csv.DictReader(open("posts.csv")):
    q = BASE%item
    print q
    c.execute(q, (id, user, title, post))

q = "delete from comments"
c.execute(q)
BASE="INSERT INTO comments VALUES(%s,%s,%s)"
for item in csv.DictReader(open("comments.csv")):
    q = BASE%item
    print q
    c.execute(q, (id, user, comment))


conn.commit()
        
