import json
import logging
import time

from django.conf import settings
from kafka import KafkaConsumer

from core.dto.pending_payment_dto import PendingPaymentDto
from core.service.remote_payment_service import RemotePaymentService


class ProcessPaymentService:
    """  """

    def __init__(self):
        self.remote_payment_service = RemotePaymentService()

    def create_consumer(self):
        try:
            return KafkaConsumer(
                settings.KAFKA_TOPIC,
                auto_offset_reset='earliest',
                bootstrap_servers=settings.KAFKA_URI,
                consumer_timeout_ms=1000,
                enable_auto_commit=False,
                value_deserializer=lambda item: json.loads(item.decode('utf-8')),
                group_id=settings.KAFKA_GROUP)
        except Exception as e:
            logging.error('Failed to check kafka events:', e)
            logging.error('Trying again in few seconds')
            time.sleep(10)
            return self.create_consumer()

    def process(self) -> None:
        """  """
        consumer = self.create_consumer()
        for pending_payment in consumer:
            logging.info(f"Processando pagamento da consulta {pending_payment.value.get('appointment_id')}")
            try:
                self.remote_payment_service.send(PendingPaymentDto().from_dict(pending_payment.value))
                consumer.commit()
                logging.info(f"Processamento do pagamento da consulta {pending_payment.value.get('appointment_id')} concluído!")
            except Exception:
                logging.exception(f"Ocorreu um erro ao processar o pagamento {pending_payment.value.get('appointment_id')}")



