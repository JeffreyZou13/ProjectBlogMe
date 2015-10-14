#ToDo

_ideas for extra stuff we can do is in italics_

###UX
- [ ] home page (home.html)
	- [ ] blog title
	- [ ] short description
	- [X] link to login **[BW]**
- [ ] login page (login.html)
	- [X] space to enter username and password **[BW]**
	- [X] authenticate info from database of users **[AL]**
	- [ ] error message
	- [ ] link back to home page
	- [ ] _link to create user_
	- [ ] _link to forgot password sends to email on file_
- [ ] _create user page_  
- [ ] user profile page (profile.html) 
	- [X] takes username as argument **[AL]**
	- [X] displays list of blog posts by user **[AL]**
	- [ ] link to logout
	- [ ] link to create new post
- [ ] blog post page (post.html)
	- [X] takes post id # as argument **[AL]**
	- [X] displays post and post comments **[AL]**
	- [ ] button to add comment on post
	- [ ] _button to edit post_ 
- [ ] create new post page
	- [ ] space to enter post title and text 
- [ ] fancy formatting - Bootstrap?
	- [ ] nav bar?

###Backend
- [X] csv database of users (users.csv -> users.db) **[AL]**
	- [X] column for username (username text)
	- [X] column for password (password text)
	- [ ] _column for retrieval email_
- [X] csv database of blog posts (posts.csv -> posts.db) **[JZ]**
	- [X] column for post id # (id int)
	- [X] column for user who created post (user text)
	- [X] column for post title (title text)
	- [X] column for post text (post text)
	- [ ] _column for date created_
	- [ ] _column for time created_
- [X] csv database of blog post comments (comments.csv -> commments.db) **[JZ]**
	- [X] column for post id # (id int)
	- [X] column for user who commented (user text)
	- [X] column for comment text (comment text)
	- [ ] _column for date created_
	- [ ] _column for time created_
- [X] python script to create sql databases (create.py) **[JZ],[AL]**
- [X] python script to populate sql databases from csv files (populate.py) **[AL]**

###Middleware

- [X] authenticate username and password from users database **[AL]**
- [X] extract list of posts by user for profile page **[AL]**
- [X] extract list of comments for post page **[AL]**

