import datetime
from decimal import Decimal
from uuid import UUID


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

