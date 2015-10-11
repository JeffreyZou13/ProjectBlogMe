#ToDo

_ideas for extra stuff we can do is in italics_

###UX
- [ ] home page (home.html)
	- [ ] blog title
	- [ ] short description
	- [ ] link to login
- [ ] login page (login.html)
	- [ ] space to enter username and password
	- [ ] authenticate info from database of users
	- [ ] link back to home page
	- [ ] _link to forgot password sends to email on file_
- [ ] _create user page_  
- [ ] user profile page 
	- [ ] takes username as argument
	- [ ] displays list of blog posts by user
	- [ ] link to logout
	- [ ] link to create new post
- [ ] blog post page
	- [ ] takes post id # as argument
	- [ ] displays post and post comments
	- [ ] button to add comment on post
	- [ ] _button to edit post_ 
- [ ] create new post page
	- [ ] space to enter post title and text 

###Backend
- [AL] csv database of users (users.csv -> users.db)
	- [ ] column for username
	- [ ] column for password
	- [ ] _column for retrieval email_
- [ ] csv database of blog posts (posts.csv -> posts.db)
	- [ ] column for post id #
	- [ ] column for user who created post
	- [ ] _column for date created_
	- [ ] _column for time created_
	- [ ] column for post text
- [ ] csv database of blog post comments (comments.csv -> commments.db)
	- [ ] column for post id #
	- [ ] column for user who commented
	- [ ] _column for date created_
	- [ ] _column for time created_
	- [ ] column for comment text
- [ ] python script to populate sql databases from csv files (create.py)

###Middleware
- [ ] authenticate username and password from users database
- [ ] extract list of posts by user for profile page
- [ ] extract list of comments for post page
