import uuid

from django.db import models

from api.dto.consultation_dto import ConsultationDto


class ConsultationModel(models.Model):
    """ Representa o modelo relacional para a Consulta """

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    physician_id = models.UUIDField(null=False)
    patient_id = models.UUIDField(null=False)
    price = models.DecimalField(null=True, max_digits=11, decimal_places=2)

    class Meta:
        db_table = "consultation"

    def to_dto(self) -> ConsultationDto:
        return ConsultationDto(
            id=self.id,
            start_date=self.start_date,
            end_date=self.end_date,
            physician_id=self.physician_id,
            patient_id=self.patient_id,
            price=self.price,
        )
