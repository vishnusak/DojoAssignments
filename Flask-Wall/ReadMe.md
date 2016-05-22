# The challenge:
- To build a Message wall where users will be able to post a message and see messages displayed by other users.
- Allow users to post comments for any message. Show the comments on the wall
- Allow message and comment edits within 30 minutes of posting

# To DO:
- ~~DB Design~~
- ~~Login/Registration~~
- ~~Wall UI~~
- ~~General Functionality~~
  - ~~Posting Messages~~
  - ~~Posting comments under messages~~
  - ~~Allowing user to delete their messages posted within last 30 mins~~
  - ~~Logout~~
- ~~Initial test with two users over the network (able to connect, login/register, post message and comment)~~
- Figure out how to NOT hardcode the image path in CSS
- Make this look the same on IE 11 as it does on EDGE and Chrome.
- Make the wall and comment refresh efficient (delta refresh instead of full refresh)
- Fix the UX on the login and registration page
- More testing ( * not sure how or when I will get to this * )
  - Multi-user refresh / delete
  - Performance
- Make the database connectivity process configurable so that the python code doesn't have to be modified

# How to set this up:
### Python Dependencies:
- Python 2.7
- Flask
- mysqlclient
- virtualenv (optional)

### Setup:
- Run the wall-DDL.sql file to set up the DB schema and tables in MySQL

or

- Use the wall-ERD.mwb file to see the ERD and forward engineer the database from it using MySQL Workbench

- In "wall.py" change the line - * "Sql(host='localhost', db='wall-test')" * - to reflect your db server and db name

- In "MySQLConnect.py" change the line - * "def \__init__(self, host, db, user='root', pwd='root', port=3306)" * - to include your mysql username, password and port

- Fire it up

#### * Any comments, review comments or feedback is welcome. *
