import uuid

from django.db import models


class PendingPaymentModel(models.Model):
    """ Representa o modelo relacional para a pendência de pagamento """

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    appointment_id = models.UUIDField(null=False, editable=False, unique=True)
    total_price = models.DecimalField(null=True, max_digits=11, decimal_places=2)
    tries = models.PositiveIntegerField(default=0)
    processing = models.BooleanField(default=False)

    class Meta:
        db_table = "pending_payment"
