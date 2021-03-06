Features added:

Users have an editable user profile, with a join date and an about field

Application searches ticketmaster for upcoming concerts in Minnesota and loads the database with venues, artists, and shows, each day

Users are able to add notes about shows which can be in the notes page

You can add photos to a note

To run the program follow these steps:

a. Create a virtual environment

b. Activate the virtual environment

c. Go to the directory that have the requirements.txt file

d. Use "pip install -r requirements.txt" to install all packages that are being used for the project.

e. in Postgres cammand line

  CREATE DATABASE lmnop;

  CREATE USER lmnop WITH PASSWORD 'lmnop';

  ALTER USER lmnop WITH SUPERUSER;

  ALTER USER lmnop WITH CREATEDB; (for testing, so the user can create and delete test database)

f. Run python manage.py run server to see if the server is working.

If you get a Pillow not installed error, we found that if you uninstall Python, and reinstall it, the error goes away.

Screenshots

homepage
![image](https://cloud.githubusercontent.com/assets/22032833/25221512/f9434cfc-257a-11e7-80b1-a6d26f53f17c.png)

userprofile
![image](https://cloud.githubusercontent.com/assets/22032833/25221459/cd91b472-257a-11e7-885e-cde66650ffb9.png)

venue list
![image](https://cloud.githubusercontent.com/assets/22032833/25221535/10ddb334-257b-11e7-8b60-8527c2298abe.png)

Artist list
![image](https://cloud.githubusercontent.com/assets/22032833/25226029/11c1f7ca-2589-11e7-9c7f-fa35be34be3b.png)

Artist notes
![image](https://cloud.githubusercontent.com/assets/22032833/25221585/3513088a-257b-11e7-9c6b-1dd7b48baba6.png)

notes list

![image](https://cloud.githubusercontent.com/assets/17325437/25227999/3f6a2a9c-2590-11e7-8389-ab9e09e2b4ad.png)


Pagination

![image](https://cloud.githubusercontent.com/assets/17325437/25228105/abc1f922-2590-11e7-9b19-9e544180b071.png)

![image](https://cloud.githubusercontent.com/assets/17325437/25228157/eeab4496-2590-11e7-9b9c-b8cef13bfaaa.png)

![image](https://cloud.githubusercontent.com/assets/17325437/25228185/13aed654-2591-11e7-81f7-5d8d60bad3cc.png)

#LMNOP

## Live Music Notes, Opinions, Photographs

###Install postgresql

https://github.com/DjangoGirls/tutorial-extensions/blob/master/optional_postgresql_installation/README.md

Set admin password, remember it.

Start postgres running

`su postgres ` if on a mac/linux
`pg_ctl start`  enter username and password

start postgres shell with `psql`

And create a user called lmnop

```
create user lmnop with password 'password_here';
```

create a database lmnop

```
create database owner lmnop;
```

Various postgres shell commands
connect to lmnop database

```
\c lmnop
```

`\dt`    shows tables

`\d table_name`   shows info (and constraints) for a table
other sql as expected

postgres shell command cheatsheet - https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546

set environment variable called
POSTGRES_LMNOP_USER_PASSWORD
with a value of the lmnop user's password


(Mac users may need to run these commands; these one time

`sudo ln -s /Library/PosgreSQL/9.5/lib/libssl.1.0.0.dylib /usr/local/lib
sudo ln -s /Library/PosgreSQL/9.5/lib/libcrypto.1.0.0.dylib /usr/local/lib`

And this when you start a new shell; or set it permanently in .bash_profile
`export DYLD_FALLBACK_LIBRARY_PATH=/Library/PostgreSQL/9.5/lib:$DYLD_LIBRARY_PATH`
)

###To install

1. Create and activate a virtual environment. Use Python3 as the interpreter.

2. pip install -r requirements.txt and pip install social-auth-app-django if the requirements doesn't do it

3. cd LMNOP/LMNOPSite

4. python manage.py makemigrations lmn

5. python manage.py migrate

6. python manage.py runserver

Site at

127.0.0.1:8000 and localhost:8000 to login with your facebook

###Create superuser

from LMNOP/LMNOPSite

python manage.py createsuperuser

enter username and password

will be able to use these to log into admin console at

127.0.0.1:8000/admin

To run tests  (some currently fail - see Issues)

python manage.py test lmn.tests

Or just some of the tests,
python manage.py test lmn.tests.test_views
python manage.py test lmn.tests.test_views.TestUserAuthentication
python manage.py test lmn.tests.test_views.TestUserAuthentication.test_user_registration_logs_user_in



### Functional Tests with selenium

Install (upgrade to the latest version if you already have it) Firefox browser. It works best for automated functional testing with Selenium.

geckodriver needs to be in path or you need to tell Selenim where it is. Pick an approach: http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

python manage.py runserver

```
python manage.py test lmn.tests.functional_tests
```

### Test coverage

From directory with manage.py in it,

coverage run --source='.' manage.py test lmn.tests

coverage report

### Social media

install django social media auth with: pip install social-auth-app-django

add login with social media was really helpful
https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html

To login in facebook for some reason it is not working on 127.0.0.1:8000, so you have to use localhost:8000
