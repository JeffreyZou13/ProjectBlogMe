#ToDo

_ideas for extra stuff we can do is in italics_

###UX
- [ ] home page (home.html)
	- [ ] blog title
	- [ ] short description
	- [ ] link to login
- [ ] login page (login.html)
	- [ ] space to enter username and password
	- [X] authenticate info from database of users **[AL]**
	- [ ] error message
	- [ ] link back to home page
	- [ ] _link to create user_
	- [ ] _link to forgot password sends to email on file_
- [ ] _create user page_  
- [ ] user profile page (profile.html) 
	- [X] takes username as argument **[AL]**
	- [ ] displays list of blog posts by user
	- [ ] link to logout
	- [ ] link to create new post
- [ ] blog post page (post.html)
	- [X] takes post id # as argument **[AL]**
	- [ ] displays post and post comments
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
- [ ] csv database of blog posts (posts.csv -> posts.db)
	- [ ] column for post id # (id int)
	- [ ] column for user who created post (user text)
	- [ ] column for post title (title text)
	- [ ] column for post text (post text)
	- [ ] _column for date created_
	- [ ] _column for time created_
- [ ] csv database of blog post comments (comments.csv -> commments.db)
	- [ ] column for post id # (id int)
	- [ ] column for user who commented (user text)
	- [ ] column for comment text (comment text)
	- [ ] _column for date created_
	- [ ] _column for time created_
- [ ] python script to create sql databases (create.py)
- [ ] python script to populate sql databases from csv files (populate.py)

###Middleware

- [X] authenticate username and password from users database **[AL]**
- [X] extract list of posts by user for profile page **[AL]**
- [X] extract list of comments for post page **[AL]**

