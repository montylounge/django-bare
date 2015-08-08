

# Overview

A simple, bare minimum Django project template for getting a Django project started. 

The idea came from the desire to easily install and play with various reusable apps.

This project installs Django's flatpages, sites, and authentication apps so the admin is setup quickly.


# Usage

This project assumes you've created, and activated, a project virtualenv for installing project dependencies. To use the `django-admin` command below you need Django installed. This project is using Django==1.8.3.

First run the below command to create your project.

`django-admin startproject --template=https://github.com/montylounge/django-bare/archive/master.zip YOUR_PROJECTNAME DESTINATION_DIRECTORY`

Example commands to get started:

> 'mkdir src'

> `django-admin startproject --template=https://github.com/montylounge/django-bare/archive/master.zip helloworld src`

> `cd src`

> `pip install -r requirements.txt`

At this point you need to create a local database for your app. This template assumes you are naming the database the same as your project.

Once you've setup your database then you can continue...

> 'python manage.py syncdb'

> 'python manage.py migrate' 

> 'python manage.py runserver'

... and you should see the Django server run.


# Dependencies

I use dj_database_url for connecting to the project's database (normally Postgres) which means I also require psycopg2.





