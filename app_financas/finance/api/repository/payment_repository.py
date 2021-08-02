from uuid import UUID

from api.dto.payment_dto import PaymentDto
from api.models.payment_model import PaymentModel


class PaymentRepository:
    """ Camada de persistência ao dados do Pagamento """

    objects = PaymentModel.objects

    def get_by_appointment_id(self, pk: UUID) -> PaymentDto:
        """ Obtem um pagamento pelo id da consulta """
        model = self.objects.get(appointment_id=pk)
        return model.to_dto() if model else None

    def is_recorded(self, appointment_id: UUID) -> bool:
        """ Verifica se uma consulta ja foi registrada """
        return self.objects.filter(appointment_id=appointment_id).count() > 0

    def save(self, dto: PaymentDto) -> PaymentDto:
        """ Grava um registro de pagamento """
        db_model = self.objects.filter(id=dto.id).first() or PaymentModel()
        db_model.appointment_id = dto.appointment_id
        db_model.total_price = dto.total_price
        db_model.save()
        return db_model.to_dto()

