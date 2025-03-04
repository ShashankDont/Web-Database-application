# Web-Database-application
Overview

This is a Flask-based web application for managing a baking contest. Users can register for the contest, view participant lists, and see contest results. The application interacts with an SQLite database to store user and contest entry data.

Features

User Registration: Allows users to register with details such as name, age, phone number, security level, and password.

List Users: Displays a list of all registered users.

List Contest Results: Shows all baking contest entries along with voting results.

Validation: Ensures that input data is properly validated before storing it in the database.

Database Integration: Uses SQLite to store user information and contest results.

Requirements

Python 3

Flask

SQLite3

Installation and Setup

1. Clone the Repository

$ git clone <repository-url>
$ cd <repository-folder>

2. Create a Virtual Environment (Optional but Recommended)

$ python -m venv venv
$ source venv/bin/activate   # On Windows use 'venv\\Scripts\\activate'

3. Install Dependencies

$ pip install flask

4. Initialize the Database

Run the following script to create the database and tables:

$ python init_db.py

5. Run the Flask Application

$ python app.py

The application will run at http://0.0.0.0:52525/

Database Schema

The application uses SQLite with the following tables:

BakingContestPeople

Column

Type

Constraints

id

INTEGER

PRIMARY KEY, AUTOINCREMENT

name

TEXT

NOT NULL

age

INTEGER

CHECK (age > 0 AND age < 121), NOT NULL

phone_number

TEXT

NOT NULL

security_level

INTEGER

CHECK (security_level BETWEEN 1 AND 3), NOT NULL

password

TEXT

NOT NULL

BakingContestEntry

Column

Type

Constraints

entry_id

INTEGER

PRIMARY KEY, AUTOINCREMENT

user_id

INTEGER

FOREIGN KEY REFERENCES BakingContestPeople(id), NOT NULL

baking_item

TEXT

NOT NULL

num_excellent_votes

INTEGER

DEFAULT 0

num_ok_votes

INTEGER

DEFAULT 0

num_bad_votes

INTEGER

DEFAULT 0

Routes

Route

Method

Description

/

GET

Home Page

/enternew

GET

Registration Form

/add_user

POST

Adds a new user after form validation

/list_users

GET

Displays registered users

/list_results

GET

Displays baking contest results

/results

GET

Shows operation results
