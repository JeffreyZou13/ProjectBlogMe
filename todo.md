#ToDo

_ideas for extra stuff we can do is in italics_

###UX
- [ ] home page (home.html)
	- [X] blog title
	- [X] link to login 
	- [X] pic carousel
- [ ] about page 
	- [ ] short description
- [X] login page (login.html)
	- [X] space to enter username and password 
	- [X] authenticate info from database of users 
	- [X] error message 
	- [X] link back to home page
	- [X] _link to create user_
	- [ ] _link to forgot password sends to email on file_
- [X] _create user page_ (register.html) 
- [ ] profiles page 
	- [ ] list all user profiles
- [ ] user profile page (profile.html) 
	- [X] takes username as argument 
	- [X] displays list of blog posts by user 
- [ ] blog post page (post.html)
	- [X] takes post id # as argument 
	- [X] displays post and post comments 
	- [X] button to add comment on post 
	- [ ] _button to edit post_ 
- [ ] create new post page (newpost.html)
	- [X] space to enter post title and text  
- [ ] fancy formatting - Bootstrap
	- [X] nav bar 
	- [ ] if logged in, change to log out link

###Backend
- [X] csv database of users (users.csv -> users.db) 
	- [X] column for username (username text)
	- [X] column for password (password text)
	- [ ] _column for retrieval email_
- [X] csv database of blog posts (posts.csv -> posts.db) 
	- [X] column for post id # (id int)
	- [X] column for user who created post (user text)
	- [X] column for post title (title text)
	- [X] column for post text (post text)
	- [ ] _column for date created_
	- [ ] _column for time created_
- [X] csv database of blog post comments (comments.csv -> commments.db)
	- [X] column for post id # (id int)
	- [X] column for user who commented (user text)
	- [X] column for comment text (comment text)
	- [ ] _column for date created_
	- [ ] _column for time created_
- [X] python script to create sql databases (create.py) 
- [X] python script to populate sql databases from csv files (populate.py) 
- [X] secure databases 

###Middleware

- [X] authenticate username and password from users database 
- [X] extract list of posts by user for profile page 
- [X] extract list of comments for post page 
- [X] remember logged in user with session
- [X] add post to database 
- [X] add comment to database
