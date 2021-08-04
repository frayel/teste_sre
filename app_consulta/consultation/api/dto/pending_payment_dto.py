from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class PendingPaymentDto:
    """ Objeto de transferência para a pendência de pagamento """

    def __init__(self, id: UUID = None, appointment_id: UUID = None,
                 total_price: Decimal = None,
                 tries: int = None, processing: bool = None,
                 finished: bool = None):
        self.id = id
        self.appointment_id = appointment_id
        self.total_price = total_price
        self.tries = tries
        self.processing = processing
        self.finished = finished

    def from_dict(self, dict_value: dict):
        """ Carrega os valores do DTO a partir de um dict """

        self.id = dict_value["id"] if "id" in dict_value else None
        self.appointment_id = dict_value["appointment_id"] if "appointment_id" in dict_value else None
        self.total_price = dict_value["total_price"] if "total_price" in dict_value else None
        self.tries = dict_value["tries"] if "tries" in dict_value else None
        self.processing = dict_value["processing"] if "processing" in dict_value else None
        self.finished = dict_value["finished"] if "finished" in dict_value else None
        return self

