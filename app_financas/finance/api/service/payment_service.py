import logging

from api.dto.payment_dto import PaymentDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.repository.payment_repository import PaymentRepository


class PaymentService:
    """ Serviço de registro de pagamento de uma consulta """

    def __init__(self):
        self.payment_repository = PaymentRepository()

    def record(self, payment_dto: PaymentDto) -> PaymentDto:

        # Verificar se o registro já nao foi feito
        if self.payment_repository.is_recorded(payment_dto.appointment_id):
            raise InvalidOperationException(f"A consulta {payment_dto.appointment_id} já foi registrada!")

        payment_dto = self.payment_repository.save(payment_dto)
        logging.info(f"O pagamento da consuta {payment_dto.appointment_id} foi registrado.")
        return payment_dto
