import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

from api.config.consultation_config import ConsultationConfig
from api.service.process_payment_service import ProcessPaymentService

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


class SchedulerService:

    payment_service = ProcessPaymentService()

    def start(self):
        scheduler.add_job(
            self.payment_service.process,
            'interval',
            id="scheduler.process_payment",
            seconds=ConsultationConfig.scheduler_interval_seconds,
            replace_existing=True)
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.ERROR)
        scheduler.start()

        return scheduler
