#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE="consulta.settings-prd"
cd consulta
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@myproject.com', 'teste123')" | python manage.py shell
gunicorn consulta.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
