import logging
from base64 import b64encode

import requests
from django.conf import settings

from api.dto.pending_payment_dto import PendingPaymentDto
from api.repository.pending_payment_repository import PendingPaymentRepository


class RemotePaymentService:
    """ Serviço de comunicação com a api financeira """

    payment_repository = PendingPaymentRepository()

    def send(self, payment: PendingPaymentDto) -> bool:
        logging.info(f'Realizando chamda remota para {settings.FINANCE_PAYMENT_ENDPOINT}')
        user_pass = b64encode(f"{settings.API_USERNAME}:{settings.API_PASSWORD}".encode()).decode("ascii")
        headers = {'Authorization': f"Basic {user_pass}"}
        data = {
            "appointment_id": str(payment.appointment_id),
            "total_price": payment.total_price,
        }
        response = requests.post(settings.FINANCE_PAYMENT_ENDPOINT, json=data, headers=headers, timeout=10)
        if response.status_code >= 300:
            logging.error(f"Ocorreu um erro. Resposta do Servidor: {response.content.decode()}")
        response.raise_for_status()
        return True
