#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE="consultation.settings-prd"
cd consultation
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@myproject.com', 'teste123')" | python manage.py shell
# Executa o scheduler em background
setsid nohup python3 manage.py start_scheduler > /opt/app/scheduler.log 2>&1 &
# Executa a aplicação
gunicorn consultation.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
