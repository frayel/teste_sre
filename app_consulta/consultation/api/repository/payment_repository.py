from uuid import UUID

from api.dto.pending_payment_dto import PendingPaymentDto
from api.models.pending_payment_model import PendingPaymentModel
from api.converter.pending_payment_converter import PendingPaymentConverter


class PaymentRepository:
    """ Camada de persistência ao dados da Pendência de Pagamento """

    objects = PendingPaymentModel.objects
    converter = PendingPaymentConverter()

    def get_by_appointment_id(self, pk: UUID) -> PendingPaymentDto:
        return self.converter.from_model_to_dto(self.objects.get(appointment_id=pk))

    def get_process_pending(self) -> list:
        return self.converter.from_model_to_dto_list(self.objects.filter(processing=False).all())

    def save(self, dto: PendingPaymentDto) -> PendingPaymentDto:
        db_model = self.objects.filter(id=dto.id).first() or PendingPaymentModel()
        db_model.appointment_id = dto.appointment_id
        db_model.total_price = dto.total_price
        db_model.tries = dto.tries
        db_model.processing = dto.processing
        db_model.save()
        return self.converter.from_model_to_dto(db_model)


    def remove(self, appointment_id: UUID) -> None:
        self.objects.get(appointment_id=appointment_id).delete()

