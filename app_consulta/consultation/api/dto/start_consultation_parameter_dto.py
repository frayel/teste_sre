from dataclasses import dataclass
from uuid import UUID

from api.exceptions.invalid_data import InvalidDataException


@dataclass
class StartConsultationParameterDto:
    """ Objeto de parametro para api de início de consulta """

    def __init__(self, physician_id: UUID = None, patient_id: UUID = None) -> None:
        self.physician_id = physician_id
        self.patient_id = patient_id

    def from_dict(self, dict_value: dict):
        self.physician_id = dict_value["physician_id"] if "physician_id" in dict_value else None
        self.patient_id = dict_value["patient_id"] if "patient_id" in dict_value else None

        return self

    def validate(self):
        if not self.physician_id:
            raise InvalidDataException("Por favor informar o médico")

        if not self.patient_id:
            raise InvalidDataException("Por favor informar o paciente")
        return self
