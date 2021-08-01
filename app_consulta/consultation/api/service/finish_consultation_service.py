import logging

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from api.dto.consultation_dto import ConsultationDto
from api.dto.finish_consultation_parameter_dto import FinishConsultationParameterDto
from api.dto.pending_payment_dto import PendingPaymentDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.repository.consultation_repository import ConsultationRepository
from api.repository.payment_repository import PaymentRepository
from api.service.price_calculator import PriceCalculator


class FinishConsultationService:
    """ Serviço para encerramento de atendimento de uma consulta """

    consultation_repository = ConsultationRepository()
    payment_repository = PaymentRepository()
    price_calculator = PriceCalculator()

    def end(self, finish_dto: FinishConsultationParameterDto) -> ConsultationDto:

        try:
            # Localiza a consulta atraves do parametro recebido
            consultation_dto = self.consultation_repository.get_by_consultation_id(finish_dto.consultation_id)

            if consultation_dto:
                if not consultation_dto.end_date:
                    # Se a consulta ainda nao foi encerrada, calcula o preco e define o horário de término
                    consultation_dto.end_date = timezone.now()
                    consultation_dto.price = self.price_calculator.calculate(consultation_dto.start_date, consultation_dto.end_date)

                    # Registra a cobrança para ser enviada à API financeira
                    pending_payment = PendingPaymentDto(appointment_id=finish_dto.consultation_id,
                                                        total_price=consultation_dto.price,
                                                        tries=0, processing=False, finished=False)
                    self.payment_repository.save(pending_payment)

                    # Grava a Consulta como Encerrada
                    consultation_dto = self.consultation_repository.save_finish(consultation_dto)
                    logging.info(f"Consulta {consultation_dto.id} Encerrada às {consultation_dto.end_date}")
                else:
                    raise InvalidOperationException(f"A consulta {finish_dto.consultation_id} já está encerrada")

        except ObjectDoesNotExist:
            raise InvalidOperationException(f"A consulta {finish_dto.consultation_id} não foi encontrada")

        return consultation_dto

