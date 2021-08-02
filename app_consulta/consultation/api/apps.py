import sys

from django.apps import AppConfig


class ApiConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Inicia o scheduler, exceto se o parametro de inicializacao for o migrate
        if 'migrate' not in sys.argv:
            # Inicia o scheduler de processamento
            from api.service.scheduler_service import SchedulerService
            scheduler_service = SchedulerService()
            scheduler_service.reset_processing_flag()
            scheduler_service.start()

