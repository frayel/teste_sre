import logging

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from api.dto.finish_consultation_dto import FinishConsultationDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.repository.consultation_repository import ConsultationRepository
from api.repository.payment_repository import PaymentRepository
from api.service.price_calculator_service import PriceCalculatorService


class FinishConsultationService:
    """ Encerra o atendimento de uma consulta """

    consultation_repository = ConsultationRepository()
    payment_repository = PaymentRepository()
    price_calculator = PriceCalculatorService()

    def end(self, dto: FinishConsultationDto):

        try:
            consultation = self.consultation_repository.get_by_consultation_id(dto.consultation_id)

            if consultation:
                if not consultation.end_date:
                    total_price = self.price_calculator.calculate(consultation.start_date, consultation.end_date)

                    # Registra a cobrança para ser enviada à API financeira
                    self.payment_repository.save(appointment_id=dto.consultation_id, total_price=total_price)

                    # Marca a Consulta como Encerrada
                    consultation.end_date = timezone.now()
                    consultation.price = total_price
                    self.consultation_repository.save_finish(consultation)
                    logging.info(f"Consulta {consultation.id} Encerrada às {consultation.end_date}")
                else:
                    raise InvalidOperationException(f"A consulta {dto.consultation_id} já está encerrada")

        except ObjectDoesNotExist:
            raise InvalidOperationException(f"A consulta {dto.consultation_id} não foi encontrada")

        return consultation

