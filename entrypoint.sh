#!/bin/sh

# Runs migrations
python manage.py migrate

exec "$@"
