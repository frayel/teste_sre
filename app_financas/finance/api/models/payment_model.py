import uuid

from django.db import models

from api.dto.payment_dto import PaymentDto


class PaymentModel(models.Model):
    """ Representa o modelo relacional do registro de pagamento """

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    appointment_id = models.UUIDField(null=False, editable=False, unique=True)
    total_price = models.DecimalField(null=True, max_digits=11, decimal_places=2)

    class Meta:
        db_table = "payment"

    def to_dto(self) -> PaymentDto:
        return PaymentDto(
            id=self.id,
            appointment_id=self.appointment_id,
            total_price=self.total_price,
        )