from api.dto.finish_consultation_dto import FinishConsultationDto
from api.dto.start_consultation_dto import StartConsultationDto
from api.exceptions.invalid_data import InvalidDataException
from api.service.base_handler import BaseHandler


class HandlerConsultation(BaseHandler):
    """ Manipula dados da consulta
    """

    def start_consultation_from_text(self, text: str) -> StartConsultationDto:
        """ Transforma texto json em um objeto de Inicio de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["physician_id"]:
            raise InvalidDataException("Por favor informar o médico")

        if not input_dict["patient_id"]:
            raise InvalidDataException("Por favor informar o paciente")

        dto = StartConsultationDto(
            physician_id=input_dict["physician_id"],
            patient_id=input_dict["patient_id"],
        )
        return dto

    def finish_consultation_from_text(self, text: str) -> FinishConsultationDto:
        """ Transforma texto json em um objeto de Término de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["consultation_id"]:
            raise InvalidDataException("Por favor informar o identificador da consulta")

        dto = FinishConsultationDto(
            consultation_id=input_dict["consultation_id"],
        )
        return dto

