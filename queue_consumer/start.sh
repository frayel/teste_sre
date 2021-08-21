#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE="app.settings"
cd app
python manage.py migrate
python manage.py loaddata initial_data
setsid nohup python3 manage.py process_payment
