from api.models.payment_model import PaymentModel


class PaymentRepository:
    """ Acesso ao model do objeto Payment """

    objects = PaymentModel.objects

    def get_by_appointment_id(self, pk: str) -> PaymentModel:
        return self.objects.get(appointment_id=pk)

    def get_process_pending(self) -> list:
        return self.objects.filter(processing=False).all()

    def save(self, appointment_id: str, total_price: float) -> None:
        payment = PaymentModel(appointment_id=appointment_id, total_price=total_price)
        payment.save()

    def save_retry(self, appointment_id: str) -> None:
        payment = self.objects.get(appointment_id=appointment_id)
        payment.tries = payment.tries + 1
        payment.save(update_fields=['tries'])

    def remove(self, appointment_id: str) -> None:
        self.objects.get(appointment_id=appointment_id).remove()