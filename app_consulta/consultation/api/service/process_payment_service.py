import logging

from api.repository.payment_repository import PaymentRepository
from api.service.remote.remote_payment_service import RemotePaymentService


class ProcessPaymentService:
    """ Serviço para processamento dos pagamentos pendentes de envio à api financeira """

    payment_repository = PaymentRepository()
    remote_payment_service = RemotePaymentService()

    def process(self) -> None:
        for p in self.payment_repository.get_process_pending():
            logging.info(f"Processando pagamento da consulta {p.appointment_id}")
            try:
                p.tries = p.tries + 1
                p.processing = True
                self.payment_repository.save(p)
                self.remote_payment_service.send(p)
                self.payment_repository.remove(p.appointment_id)
                logging.info(f"Processamento do pagamento da consulta {p.appointment_id} concluído!")
            except Exception:
                logging.exception(f"Ocorreu um erro ao processar o pagamento {p.appointment_id}")
                p.processing = False
                self.payment_repository.save(p)

