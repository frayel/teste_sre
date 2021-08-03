from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from api.exceptions.invalid_data import InvalidDataException


@dataclass
class PaymentDto:
    """ Objeto de transferência para o registro financeiro de uma consulta """

    def __init__(self, id: int = None, appointment_id: UUID = None,
                 total_price: Decimal = None):
        self.id = id
        self.appointment_id = appointment_id
        self.total_price = total_price

    def from_dict(self, dict_value: dict):
        self.id = dict_value["id"] if "id" in dict_value else None
        self.appointment_id = dict_value["appointment_id"] if "appointment_id" in dict_value else None
        self.total_price = dict_value["total_price"] if "total_price" in dict_value else None

        if not self.appointment_id:
            raise InvalidDataException("Por favor informar o identificador da consulta")

        if self.total_price is None:
            raise InvalidDataException("Por favor informar o valor total")

        return self