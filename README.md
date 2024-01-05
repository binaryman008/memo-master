# Memo Master

A backend having API's for the notes application.

## Features
1. User can create an account
2. Uses JWT Authentication for Login
3. Implemented Elastic Search for high performance index based searching of keywords
4. Rate Limiter applied

## Technologies
Python, Django, Django Rest Framework, Postgres, Elastic Search

## Requirements
1. Python 3.8 <=
2. Postgres@15
3. Java 8 (for elastic search)
3. ElasticSearch server up and running [Download Here](https://www.elastic.co/downloads/elasticsearch)

## Installation and Project Setup
1. Clone the repository
2. `cd memo-master`
3. create a virtual environment `python3 -m venv env`
4. Activate the virtual environment `source env/bin/activate`
5. Install python packages `pip install -r requirements.txt`
6. Create a Database in postgres. Run the command from terminal `createdb -U postgres notes`
7. Run migration files `python manage.py migrate`
8. Create a Logs folder in the memo-master directory `mkdir Logs`
9. Create a config file for the django server. `touch config.py`
10. Copy all the keys from `config.py.example` into `config.py`
11. Change the LOG_FILE_LOCATION in `config.py` with the path of Logs folder created above.
12. Run the python server `python manage.py runserver`

The server should be up and running on `http://localhost:8000`

## Operating Instructions

The url for the endpoint will look like this for the signup:
`http://localhost:8000/api/auth/signup`

### The curl requests for the apis integrated are as below:
1. Signup
`curl --location 'localhost:8000/api/auth/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Test",
    "last_name": "User",
    "password": "testpassword",
    "email": "test@gmail.com"
}'`

2. Login
`curl --location 'localhost:8000/api/auth/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "test@gmail.com",
    "password": "testpassword"
}'`

3. Submit a note for the authenticated User
`curl --location 'localhost:8000/api/notes' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Heading",
    "content": "To do things"
}'`

4. Get all Notes for the authenticated User
`curl --location 'localhost:8000/api/notes' \
--header 'Authorization: Bearer {{access_token}}'`

5. Get a Note by Id
`curl --location 'localhost:8000/api/notes/{notes_id}/' \
--header 'Authorization: Bearer {{access_token}}'`

6. Search all notes based on keyword
`curl --location 'http://localhost:8000/api/notes/search/?q=keyword' \
--header 'Authorization: Bearer {{access_token}}'`

7. PUT method on notes app
`curl --location --request PUT 'localhost:8000/api/notes/{notes_id}/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{"title":"new data",
"content":"newdata 2"
}'`

8. Delete a note
`curl --location --request DELETE 'localhost:8000/api/notes/4cea9213-b999-42d4-ad03-c47a8fc4b8de/' \
--header 'Authorization: Bearer {{access_token}}'`

9. Share a note
`curl --location 'localhost:8000/api/notes/0cde8e91-0772-47c0-a09b-d34fb17cbafa/share' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{"notes_id":"d103ca1e-645e-4e61-89b5-da3729c660eb"}'`


## Running tests
The integration tests and unit tests for serializers, models and rate limiter are covered in this project.
To run tests, run the following commands:
1. `python manage.py test notes.tests`
2. `python manage.py test users.tests`