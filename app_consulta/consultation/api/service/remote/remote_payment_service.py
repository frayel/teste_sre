import logging

from api.dto.start_consultation_dto import StartConsultationDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.models.consultation_model import ConsultationModel
from api.repository.consultation_repository import ConsultationRepository
from api.repository.payment_repository import PaymentRepository


class RemotePaymentService:

    payment_repository = PaymentRepository()

    def send(self, dto, PaymentDto) -> None:
        for p in self.payment_repository.get_process_pending():
            logging.info(f'Processando pagamento {p.appointment_id}')
            self.payment_repository.save_retry(appointment_id)
            self.payment_repository.remove(appointment_id)

