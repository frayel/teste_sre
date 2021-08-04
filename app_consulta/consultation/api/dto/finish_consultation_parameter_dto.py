import datetime
from dataclasses import dataclass
from uuid import UUID

from api.exceptions.invalid_data import InvalidDataException


@dataclass
class FinishConsultationParameterDto:
    """ Objeto de parâmetro para api de termino de consulta """

    def __init__(self, consultation_id: UUID = None, end_date: datetime = None) -> None:
        self.consultation_id = consultation_id
        self.end_date = end_date

    def from_dict(self, dict_value: dict):
        """ Carrega os valores do DTO a partir de um dict """

        self.consultation_id = dict_value["consultation_id"] if "consultation_id" in dict_value else None
        self.end_date = datetime.datetime.strptime(dict_value["end_date"], "%Y-%m-%dT%H:%M:%S") if "end_date" in dict_value else None
        return self

    def validate(self):
        """ Valida se os dados do DTO são válidos """

        if not self.consultation_id:
            raise InvalidDataException("Por favor informar o identificador da consulta")

        return self

