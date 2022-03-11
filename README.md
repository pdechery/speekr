# Posterr

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

Run the app
`python manage.py runserver`

Access it on a browser at `http:127.0.0.1:8000`
Available pages are: Home ('/') and profile page ('/profile/{user_id}')
User id's in the database go from 1 to 9, so an example would be ('/profile/2')

**Note**
Since there's not an authentication system available, an "authenticaded" user id is given it the frontend via the "auth_user" variable. It can be modified as needed (1 to 9, as explained above).

## Planning

### Questions

- Replying is allowed to any user or only those I follow/following me?
- We already have a limit to five posts a day per user. Replies will fit in this rule?
- There should be a limit of replies a post can have?
- How the replies should be displayed in the feed? 
- Should we have some moderation, in case of SPAM or offensive replies? Or hate-speech? 
- The original poster should opt-in for replies in his posts?

### Assumptions

These replies should be reached only from the profile page. Be it the auth user's or some user profile he's accessing. We could use a tab, and the data should be loaded asynchronously.
I'd do a new model in Django to persist the replies, with a Many to One relation with the post.
Fields would be: reply, user who made it, date and particular post.

## Critique

##### Isolation of classes
There must be a better organization in the backend's classes. Right now all the models live in the same file, for example.
The whole code base should be refactored to allow isolation of entities, so everyone could benefit from better maintenance.

##### JS Framework
The frontend also suffer from this same problem, and a lot of code is repeated. I'd use also Vue's build system as well as research other solutions proposed by this framework to allow better organization and separation of responsibilites.

##### Infrastructure
With more time I'd do a Docker environment instead of using Django's built-in server. Doing so I could simulate Productions's environment, among other benefits.

##### Caching
The database queries could be improved but the piority should be have some caching service, to store all data in the Home page, for instance. This could be Redis, or even Django caching solution itself. I'd have to study the existing solutions deeplier to propose something.

##### paaS and Load test
Since this test uses Django's built-in webserver, obviously we should move to a real webserver, like Nginx, and have a paaS service to support auto-scaling. Load tests would help to identify the app's real needs. The Locust python package could help with that.


