from uuid import UUID

from api.dto.finish_consultation_dto import FinishConsultationDto
from api.exceptions.invalid_data import InvalidDataException
from api.converter.base_converter import BaseConverter


class FinishConsultationConverter(BaseConverter):
    """ Converte dados para o DTO de entrada na api de término de consulta
    """

    def from_text(self, text: str) -> FinishConsultationDto:
        """ Transforma texto json em um objeto de Término de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["consultation_id"]:
            raise InvalidDataException("Por favor informar o identificador da consulta")

        dto = FinishConsultationDto(
            consultation_id=UUID(input_dict["consultation_id"]),
        )
        return dto

