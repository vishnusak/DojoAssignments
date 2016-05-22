# The ask:
### Make 7 restful routes to manage the user database

## Done:
1. '/' and '/users' will display the main page
2. '/users/new' - for displaying a add-new-user page
3. '/users/create' - for adding new user to database
4. '/users/< id >' - for seeing details of the specific user
5. '/users/< id >/edit' - for displaying the edit-user-details page
6. '/users/< id >/update' - for updating the details of existing user
7. '/users/< id >/destroy' - for deleting the details of existing user

## Not Done:
- Validations: If a route - e.g., /users/2/edit - is entered and the record with user_id = 2 is not present, the page crashes since that condition is not handled
- Except for the ID, none of the columns are unique. This will lead to issues down the line (add multiple users with the same name and email id!!)

## Dependencies:
- As usual, the dependencies to run this are
  + Python 2.7
  + Flask
  + mysqlclient
  + virtualenv (optional)

- Since this involves just one table, I am not attaching the DDL. The users table must have the following:
  + id - INT
  + first_name - varchar(45)
  + last_name - varchar(45)
  + email - varchar(45)
  + created_at - DATETIME
  + modified_at - DATETIME
