import uuid

from django.db import models

from api.dto.pending_payment_dto import PendingPaymentDto


class PendingPaymentModel(models.Model):
    """ Representa o modelo relacional para a pendência de pagamento """

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    appointment_id = models.UUIDField(null=False, editable=False, unique=True)
    total_price = models.DecimalField(null=True, max_digits=11, decimal_places=2)
    tries = models.PositiveIntegerField(default=0)
    processing = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    class Meta:
        db_table = "pending_payment"

    def to_dto(self) -> PendingPaymentDto:
        """ Transforma o objeto model em um DTO """

        return PendingPaymentDto(
            id=self.id,
            appointment_id=self.appointment_id,
            total_price=self.total_price,
            tries=self.tries,
            processing=self.processing,
            finished=self.finished,
        )
