from decimal import Decimal
from uuid import UUID


class PendingPaymentDto:
    """ Objeto de transferência para a pendência de pagamento """

    def __init__(self, id: int = None, appointment_id: UUID = None,
                 total_price: Decimal = None,
                 tries: int = None, processing: bool = None,
                 finished: bool = None):
        self.id = id
        self.appointment_id = appointment_id
        self.total_price = total_price
        self.tries = tries
        self.processing = processing
        self.finished = finished

