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

q = "delete from posts"
c.execute(q)
BASE="INSERT INTO posts VALUES('%(id)s','%(user)s','%(title)s','%(post)s','%(date)s','%(time)s')"
for item in csv.DictReader(open("posts.csv")):
    q = BASE%item
    print q
    c.execute(q)

q = "delete from comments"
c.execute(q)
BASE="INSERT INTO comments VALUES('%(id)s','%(user)s','%(comment)s','%(date)s','%(time)s')"
for item in csv.DictReader(open("comments.csv")):
    q = BASE%item
    print q
    c.execute(q)


conn.commit()
        
