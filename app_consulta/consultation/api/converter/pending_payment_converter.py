from api.dto.pending_payment_dto import PendingPaymentDto
from api.models.pending_payment_model import PendingPaymentModel
from api.converter.base_converter import BaseConverter


class PendingPaymentConverter(BaseConverter):
    """ Converte dados do PendingPayment entre Model e DTO
    """

    def from_dto_to_model(self, dto: PendingPaymentDto, model: PendingPaymentModel) -> PendingPaymentModel:
        """ Transforma um DTO em um objeto Model """
        if not model:
            model = PendingPaymentModel(id=dto.id)
        model.appointment_id = dto.appointment_id
        model.total_price = dto.total_price
        model.tries = dto.tries
        model.processing = dto.processing
        return model

    def from_model_to_dto(self, model: PendingPaymentModel) -> PendingPaymentDto:
        """ Transforma um objeto Model em um DTO """
        dto = PendingPaymentDto(
            appointment_id=model.appointment_id,
            total_price=model.total_price,
            tries=model.tries,
            processing=model.processing,
        ) if model else None
        return dto

    def from_model_to_dto_list(self, model_list: list) -> list:
        return [self.from_model_to_dto(model) for model in model_list]

