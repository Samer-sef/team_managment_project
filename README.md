# team_managment_project
A project built using Django framework to store/update/delete team members.

# Getting Started

### Prerequisites
Python: Install the latest version of Python compatible with Django from the official Python website.
PIP (Python Package Installer): Verify PIP is installed by running pip --version in your command prompt or terminal.
Django Framework: Install Django using the command pip install django.

### Installing
Since the db.sqlite3 file is uploaded in the repo, you only need to execute this command to run the project:
```
python ./manage.py runserver
```

Making changes on the models require migrating the db before rerunning the app:
```
python manage.py migrate
python ./manage.py runserver
```

### The details for the current superuser:
    username: admin
    password: admin
