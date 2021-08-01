from uuid import UUID

from api.converter.payment_converter import PaymentConverter
from api.dto.payment_dto import PaymentDto
from api.models.payment_model import PaymentModel


class PaymentRepository:
    """ Camada de persistência ao dados do Pagamento """

    objects = PaymentModel.objects
    converter = PaymentConverter()

    def get_by_appointment_id(self, pk: UUID) -> PaymentDto:
        return self.converter.from_model_to_dto(self.objects.get(appointment_id=pk))

    def is_recorded(self, appointment_id: UUID) -> bool:
        return self.objects.filter(appointment_id=appointment_id).count() > 0

    def save(self, dto: PaymentDto) -> PaymentDto:
        db_model = self.objects.filter(id=dto.id).first() or PaymentModel()
        db_model.appointment_id = dto.appointment_id
        db_model.total_price = dto.total_price
        db_model.save()
        return self.converter.from_model_to_dto(db_model)

    def remove(self, appointment_id: UUID) -> None:
        self.objects.get(appointment_id=appointment_id).delete()

