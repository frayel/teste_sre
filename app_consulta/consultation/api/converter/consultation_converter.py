import json
from uuid import UUID

from django.core.serializers.json import DjangoJSONEncoder

from api.converter.base_converter import BaseConverter
from api.dto.consultation_dto import ConsultationDto
from api.dto.finish_consultation_parameter_dto import FinishConsultationParameterDto
from api.dto.start_consultation_parameter_dto import StartConsultationParameterDto
from api.exceptions.invalid_data import InvalidDataException
from api.models.consultation_model import ConsultationModel


class ConsultationConverter(BaseConverter):
    """ Converte dados da Consulta
    """

    def from_model_to_dto(self, model: ConsultationModel) -> ConsultationDto:
        """ Transforma um objeto Model em um DTO """
        dto = ConsultationDto(
            id=model.id,
            start_date=model.start_date,
            end_date=model.end_date,
            physician_id=model.physician_id,
            patient_id=model.patient_id,
            price=model.price,
        ) if model else None
        return dto

    def dto_to_json(self, dto: ConsultationDto) -> str:
        """ Transforma o dto em json """
        return json.dumps(dto.__dict__, ensure_ascii=False, cls=DjangoJSONEncoder)

    def finish_data_from_text(self, text: str) -> FinishConsultationParameterDto:
        """ Transforma texto json em um parametro de Término de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["consultation_id"]:
            raise InvalidDataException("Por favor informar o identificador da consulta")

        dto = FinishConsultationParameterDto(
            consultation_id=UUID(input_dict["consultation_id"]),
        )
        return dto

    def start_data_from_text(self, text: str) -> StartConsultationParameterDto:
        """ Transforma texto json em um parametro de Inicio de Consulta """

        input_dict = self._text_to_dict(text)

        if not input_dict["physician_id"]:
            raise InvalidDataException("Por favor informar o médico")

        if not input_dict["patient_id"]:
            raise InvalidDataException("Por favor informar o paciente")

        dto = StartConsultationParameterDto(
            physician_id=UUID(input_dict["physician_id"]),
            patient_id=UUID(input_dict["patient_id"]),
        )
        return dto