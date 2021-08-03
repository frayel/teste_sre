import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from django.core.management.base import BaseCommand

from api.service.scheduler_service import SchedulerService

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = '''Este script coloca o scheduler em execução em um processo separado do processo da aplicação'''

    def handle(self, *args, **options):
        scheduler_service = SchedulerService(BlockingScheduler(settings.SCHEDULER_CONFIG))
        try:
            scheduler_service.reset_processing_flag()
            scheduler_service.start()

        except KeyboardInterrupt:
            scheduler_service.stop()
