from uuid import UUID

from api.converter.base_converter import BaseConverter
from api.dto.payment_dto import PaymentDto
from api.exceptions.invalid_data import InvalidDataException
from api.models.payment_model import PaymentModel


class PaymentConverter(BaseConverter):
    """ Converte dados do Pagamento entre Model e DTO
    """

    def from_text(self, text: str) -> PaymentDto:
        """ Transforma texto json em um objeto de Pagamento """

        input_dict = self._text_to_dict(text)

        if not input_dict["appointment_id"]:
            raise InvalidDataException("Por favor informar o identificador da consulta")

        if input_dict["total_price"] is None:
            raise InvalidDataException("Por favor informar o valor total")

        dto = PaymentDto(
            appointment_id=UUID(input_dict["appointment_id"]),
            total_price=input_dict["total_price"],
        )
        return dto

    def from_model_to_dto(self, model: PaymentModel) -> PaymentDto:
        """ Transforma um objeto Model em um DTO """
        dto = PaymentDto(
            id=model.id,
            appointment_id=model.appointment_id,
            total_price=model.total_price,
        ) if model else None
        return dto

    def from_model_to_dto_list(self, model_list: list) -> list:
        return [self.from_model_to_dto(model) for model in model_list]

