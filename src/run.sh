#!/bin/bash

# run migrate
cd app
python manage.py migrate
python manage.py collectstatic --noinput

# back to root
cd ..

/usr/local/bin/uwsgi uwsgi.ini
