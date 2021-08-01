import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

from api.service.process_payment_service import ProcessPaymentService

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


class SchedulerService:
    """ Agendador de tarefa pra processar os pagamentos pendentes de envio à api financeira """

    payment_service = ProcessPaymentService()

    def start(self) -> BackgroundScheduler:
        scheduler.add_job(
            self.payment_service.process,
            'interval',
            id="scheduler.process_payment",
            seconds=settings.SCHEDULER_INTERVAL_SECONDS,
            replace_existing=True)
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.ERROR)
        scheduler.start()

        return scheduler
