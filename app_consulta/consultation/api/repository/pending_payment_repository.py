from uuid import UUID

from api.dto.pending_payment_dto import PendingPaymentDto
from api.models.pending_payment_model import PendingPaymentModel


class PendingPaymentRepository:
    """ Camada de persistência de dados da Pendência de Pagamento """

    def __init__(self):
        self.objects = PendingPaymentModel.objects

    def get_by_appointment_id(self, pk: UUID) -> PendingPaymentDto:
        """ Obtem uma pendencia de pagamento pelo id da consulta """
        model = self.objects.get(appointment_id=pk)
        return model.to_dto() if model else None

    def get_process_pending(self) -> list:
        """ Obtem uma lista com todos os pagamentos pendentes de processamento """
        model_list = self.objects.filter(processing=False, finished=False).all()
        return [model.to_dto() for model in model_list]

    def save(self, dto: PendingPaymentDto) -> PendingPaymentDto:
        """ Grava um registro de pendencia de pagamento """
        db_model = self.objects.filter(id=dto.id).first() or PendingPaymentModel()
        db_model.appointment_id = dto.appointment_id
        db_model.total_price = dto.total_price
        db_model.tries = dto.tries
        db_model.processing = dto.processing
        db_model.finished = dto.finished
        db_model.save()
        return db_model.to_dto()

    def finish(self, appointment_id: UUID) -> PendingPaymentDto:
        """ Marca o registro de de pendenencia como processada """
        db_model = self.objects.get(appointment_id=appointment_id)
        db_model.finished = True
        db_model.processing = False
        db_model.save(update_fields=['finished', 'processing'])
        return db_model.to_dto()

    def reset_processing_flag(self):
        """ Define a flag de processamento para false, de todos os pagamentos pendentes. """
        updated_rows = self.objects.filter(processing=True, finished=False).update(processing=False)
        return updated_rows

