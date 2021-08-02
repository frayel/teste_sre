from uuid import UUID

from api.exceptions.invalid_data import InvalidDataException


class FinishConsultationParameterDto:
    """ Objeto de parametro para api de termino de consulta """

    def __init__(self, consultation_id: UUID = None) -> None:
        self.consultation_id = consultation_id

    def from_dict(self, dict_value: dict):
        self.consultation_id = dict_value["consultation_id"] if "consultation_id" in dict_value else None
        return self

    def validate(self):
        if not self.consultation_id:
            raise InvalidDataException("Por favor informar o identificador da consulta")
        return self