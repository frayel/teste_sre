import logging

from api.dto.start_consultation_dto import StartConsultationDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.models.consultation_model import ConsultationModel
from api.repository.consultation_repository import ConsultationRepository
from api.repository.payment_repository import PaymentRepository
from api.service.remote.remote_payment_service import RemotePaymentService


class ProcessPaymentService:

    payment_repository = PaymentRepository()
    remote_payment_service = RemotePaymentService()

    def process(self) -> None:
        for p in self.payment_repository.get_process_pending():
            logging.info(f'Processando pagamento {p.appointment_id}')
            self.remote_payment_service.send(p)

