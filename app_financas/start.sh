#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE="finance.settings"
cd finance
python manage.py migrate
python manage.py loaddata initial_data
gunicorn finance.wsgi --user www-data --bind 0.0.0.0:8020 --workers 3
