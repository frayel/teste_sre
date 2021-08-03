import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

from api.repository.pending_payment_repository import PendingPaymentRepository
from api.service.process_payment_service import ProcessPaymentService

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


class SchedulerService:
    """ Agendador de tarefa pra processar os pagamentos pendentes de envio à api financeira """

    payment_service = ProcessPaymentService()
    repository = PendingPaymentRepository()

    def start(self) -> BackgroundScheduler:
        """ Inicia o agendador para processar os pagamentos pendentes no intervalo determinado """

        scheduler.add_job(
            self.payment_service.process,
            'interval',
            id="scheduler.process_payment",
            seconds=settings.SCHEDULER_INTERVAL_SECONDS,
            replace_existing=True)

        logging.getLogger('apscheduler').setLevel(logging.ERROR)
        scheduler.start()

        return scheduler

    def reset_processing_flag(self):
        """ Define a flag de processamento para false, de todos os pagamentos pendentes.
            Este método será chamado quando a aplicação subir e garantir que todos os pagamentos
            sejam re-processados após uma queda do scheduler. """

        updated = self.repository.reset_processing_flag()

        if updated > 0:
            logging.info(f"{updated} registros foram liberados para serem reprocessados.")




