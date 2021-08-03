import logging
import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):

        logging.info(f'Aplicação iniciada pid={os.getpid()}...')

        # Inicia o scheduler de processamento caso esteja rodando em desenvolvimento.
        # Se a aplicação estiver rodando pelo gunicorn, executar o comando "management.py start_scheduler"
        if 'runserver' in sys.argv and os.environ.get('RUN_MAIN', None) != 'true':
            from api.service.scheduler_service import SchedulerService
            scheduler_service = SchedulerService(BackgroundScheduler(settings.SCHEDULER_CONFIG))
            scheduler_service.reset_processing_flag()
            scheduler_service.start()

