# This is the login-registration assignment from Flask+MySQL

## What it includes:

- The login.sql has the queries for creating a database with one table called users. This table holds first and last names, email, password, created and updated times
- The MySQLConnect.py and Validation.py are hopefully self-explanatory
- login.py is the server
- There are 2 templates: login.html for the login/registration pages; main.html for displaying logged in user after login. The static folder has the related css and js files.

## What it doesn't include:

- the virtual env is not included. Please set up your own venv for running this.
- The venv would need the following
  - python 2.7
  - flask
  - mysqlclient
  - bcrypt

## What is done:

- Login for existing users
- Registration for new users
- Validations for all fields

## To DO:

- Every time an error message is flashed, existing values in all the form fields disappear. This has to be addressed
- After logging in and seeing main.html, logout option should be provided.
- AJAX instead of full page reload.
