import uuid

from django.db import models


class Consulta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    physician_id = models.UUIDField(null=False)
    patient_id = models.UUIDField(null=False)
    price = models.DecimalField(null=True, max_digits=11, decimal_places=2)
