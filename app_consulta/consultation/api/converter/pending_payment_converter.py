from api.converter.base_converter import BaseConverter
from api.dto.pending_payment_dto import PendingPaymentDto
from api.models.pending_payment_model import PendingPaymentModel


class PendingPaymentConverter(BaseConverter):
    """ Converte dados do PendingPayment entre Model e DTO
    """

    def from_model_to_dto(self, model: PendingPaymentModel) -> PendingPaymentDto:
        """ Transforma um objeto Model em um DTO """
        dto = PendingPaymentDto(
            id=model.id,
            appointment_id=model.appointment_id,
            total_price=model.total_price,
            tries=model.tries,
            processing=model.processing,
        ) if model else None
        return dto

    def from_model_to_dto_list(self, model_list: list) -> list:
        return [self.from_model_to_dto(model) for model in model_list]

