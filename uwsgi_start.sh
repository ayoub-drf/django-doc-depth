#!/bin/bash

uwsgi --ini uwsgi.ini

# uwsgi --chdir=/home/x/Desktop/django-doc-depth \
#     --module=dj.wsgi:application \
#     --env DJANGO_SETTINGS_MODULE=dj.settings \
#     --master --pidfile=/tmp/project-master.pid \
#     --http=:8000 \
#     --processes=2 \
#     --harakiri=20 \
#     --max-requests=5000 \
#     --vacuum \
#     --home=/home/x/Desktop/django-doc-depth/.venv \
#     --buffer-size=32768



