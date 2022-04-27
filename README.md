# Speekr

This is a rudimentary Twitter app. It's possible to write posts, follow other users and repost and/or comment their posts.

I build this with the following tools:

- Django 4.0
- Django Rest Framework 3.13
- Vue.js
- Sqlite

I'm currently working in this project trying to add a better interface between other improvements.

### Build Steps  

This app is built with Django Framework, version 4, and uses the Django Rest package to support the REST API.
In the frontend, Vue.js is used to fetch data from that API and render it in the HTML templates.
A sqlite database is included with initial data, as well as fixtures with users and posts.

To run this app, please follow these steps. 
*OBS: These commands are for Linux environments.*

Inside app's directory, create a virtual environment using venv.
`python3 -m venv venv`

Run the virtual environment
`source venv/bin/activate`

Install packages
`pip install -r requirements.txt`

Run the app
`python manage.py runserver`

Access it on a browser at `http:127.0.0.1:8000`
Available pages are: Home ('/') and profile page ('/profile/{user_id}')
User id's in the database go from 1 to 9, so an example would be ('/profile/2')

**Note**
Since there's not an authentication system available, an "authenticaded" user id is given it the frontend via the "auth_user" variable. It can be modified as needed (1 to 9, as explained above).



