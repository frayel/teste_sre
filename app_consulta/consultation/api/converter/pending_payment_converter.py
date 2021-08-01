from api.dto.pending_payment_dto import PendingPaymentDto
from api.models.pending_payment_model import PendingPaymentModel


class PendingPaymentConverter:
    """ Converte dados do PendingPayment
    """

    def from_model_to_dto(self, model: PendingPaymentModel) -> PendingPaymentDto:
        """ Transforma um objeto Model em um DTO """
        dto = PendingPaymentDto(
            id=model.id,
            appointment_id=model.appointment_id,
            total_price=model.total_price,
            tries=model.tries,
            processing=model.processing,
            finished=model.finished,
        ) if model else None
        return dto


