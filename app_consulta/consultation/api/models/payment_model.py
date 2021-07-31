import uuid

from django.db import models


class PaymentModel(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.DecimalField(null=True, max_digits=11, decimal_places=2)
    tries = models.PositiveIntegerField(default=0)
    processing = models.BooleanField(default=False)

    class Meta:
        db_table = "payment"
