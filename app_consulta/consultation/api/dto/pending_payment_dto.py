from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class PendingPaymentDto:
    """ Objeto de transferĂȘncia para a pendĂȘncia de pagamento """

    def __init__(self, id: UUID = None, appointment_id: UUID = None,
                 total_price: Decimal = None):
        self.id = id
        self.appointment_id = appointment_id
        self.total_price = total_price


    def from_dict(self, dict_value: dict):
        """ Carrega os valores do DTO a partir de um dict """

        self.id = dict_value["id"] if "id" in dict_value else None
        self.appointment_id = dict_value["appointment_id"] if "appointment_id" in dict_value else None
        self.total_price = dict_value["total_price"] if "total_price" in dict_value else None

        return self

