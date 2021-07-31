from endpoint.dto.inicio_consulta_dto import InicioConsultaDto
from endpoint.service.base_handler import BaseHandler


class HandlerConsulta(BaseHandler):
    """ Manipula dados da consulta
    """

    def inicio_consulta_from_text(self, text: str) -> InicioConsultaDto:
        """ Transforma texto json em um objeto de Inicio de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["physician_id"]:
            raise Exception("Por favor informar o médico")

        if not input_dict["patient_id"]:
            raise Exception("Por favor informar o paciente")

        dto = InicioConsultaDto(
            physician_id=input_dict["physician_id"],
            patient_id=input_dict["patient_id"],
        )
        return dto
