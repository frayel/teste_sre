import datetime
from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class ConsultationDto:
    """ Objeto de transferencia para a consulta """

    def __init__(self,
                 id: UUID = None, start_date: datetime = None, end_date: datetime = None,
                 physician_id: UUID = None, patient_id: UUID = None, price: Decimal = None):

        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.physician_id = physician_id
        self.patient_id = patient_id
        self.price = price

    def from_dict(self, dict_value: dict):
        self.id = dict_value["id"] if "id" in dict_value else None
        self.start_date = dict_value["start_date"] if "start_date" in dict_value else None
        self.end_date = dict_value["end_date"] if "end_date" in dict_value else None
        self.physician_id = dict_value["physician_id"] if "physician_id" in dict_value else None
        self.patient_id = dict_value["patient_id"] if "patient_id" in dict_value else None
        self.price = dict_value["price"] if "price" in dict_value else None
        return self