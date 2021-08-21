import json
import logging

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.utils import timezone
from kafka import KafkaProducer

from api.dto.consultation_dto import ConsultationDto
from api.dto.finish_consultation_parameter_dto import FinishConsultationParameterDto
from api.dto.pending_payment_dto import PendingPaymentDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.repository.consultation_repository import ConsultationRepository
from api.service.price_calculator import PriceCalculator


class FinishConsultationService:
    """ Serviço para encerramento de atendimento de uma consulta
        Executado em uma transação atômica, portanto em caso de erro, as alterações nao serao gravadas
    """

    def __init__(self):
        self.consultation_repository = ConsultationRepository()
        self.price_calculator = PriceCalculator()

    @transaction.atomic
    def end(self, finish_dto: FinishConsultationParameterDto) -> ConsultationDto:
        """ Realiza o encerramento do atendimento e grava o pagamento para ser processado pelo scheduler.
            o decorator transaction.atomic garante que o método será realizado em uma transação atômica, ou seja,
            haverá rollback em caso de erro."""

        try:
            # Localiza a consulta atraves do parametro recebido
            consultation_dto = self.consultation_repository.get_by_consultation_id(finish_dto.consultation_id)

            if consultation_dto:
                if not consultation_dto.end_date:
                    # Se a consulta ainda não foi encerrada, calcula o preco e define o horário de término
                    consultation_dto.end_date = finish_dto.end_date if finish_dto.end_date else timezone.now()
                    consultation_dto.price = self.price_calculator.calculate(consultation_dto.start_date, consultation_dto.end_date)

                    # Registra a cobrança para ser enviada à API financeira
                    pending_payment = PendingPaymentDto(appointment_id=finish_dto.consultation_id,
                                                        total_price=consultation_dto.price)
                    producer = KafkaProducer(bootstrap_servers=settings.KAFKA_URI,
                                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
                    producer.send(settings.KAFKA_TOPIC, pending_payment.__dict__)
                    producer.flush()
                    producer.close()

                    # Grava a Consulta como Encerrada
                    consultation_dto = self.consultation_repository.save_finish(consultation_dto)
                    logging.info(f"Consulta {consultation_dto.id} Encerrada às {consultation_dto.end_date}")
                else:
                    raise InvalidOperationException(f"A consulta {finish_dto.consultation_id} já está encerrada")

        except ObjectDoesNotExist:
            raise InvalidOperationException(f"A consulta {finish_dto.consultation_id} não foi encontrada")

        return consultation_dto

