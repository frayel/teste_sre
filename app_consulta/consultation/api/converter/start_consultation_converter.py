from uuid import UUID

from api.dto.start_consultation_dto import StartConsultationDto
from api.exceptions.invalid_data import InvalidDataException
from api.converter.base_converter import BaseConverter


class StartConsultationConverter(BaseConverter):
    """ Converte dados para o DTO de entrada na api de início de consulta
    """

    def from_text(self, text: str) -> StartConsultationDto:
        """ Transforma texto json em um objeto de Inicio de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["physician_id"]:
            raise InvalidDataException("Por favor informar o médico")

        if not input_dict["patient_id"]:
            raise InvalidDataException("Por favor informar o paciente")

        dto = StartConsultationDto(
            physician_id=UUID(input_dict["physician_id"]),
            patient_id=UUID(input_dict["patient_id"]),
        )
        return dto
