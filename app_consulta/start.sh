#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE="consultation.settings"
cd consultation
python manage.py migrate
python manage.py loaddata initial_data
gunicorn consultation.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
