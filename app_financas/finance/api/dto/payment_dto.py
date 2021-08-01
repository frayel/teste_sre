from decimal import Decimal
from uuid import UUID


class PaymentDto:
    """ Objeto de transferência para o pagamento """

    def __init__(self, id: int = None, appointment_id: UUID = None,
                 total_price: Decimal = None):
        self.id = id
        self.appointment_id = appointment_id
        self.total_price = total_price

