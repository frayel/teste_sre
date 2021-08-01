import datetime
import logging
from decimal import Decimal

from api.config.consultation_config import ConsultationConfig
from api.exceptions.invalid_data import InvalidDataException


class PriceCalculator:
    """ Calcula o preço de uma consulta
        Obs: O valor mínimo será de o valor de 1h e os minutos excedentes serão proporcionais """

    # Arquivo de configuração com os parametros do calculo
    config = ConsultationConfig()

    def calculate(self, start_date: datetime, end_date: datetime) -> Decimal:
        logging.info('Iniciando o cálculo de preços')
        if start_date and end_date:
            if end_date > start_date:
                duration = end_date - start_date
                hours = round(duration.total_seconds() / 3600, 2) if duration.total_seconds() > 3600 else 1
                price = round(self.config.price_per_hour * hours, 2)
                logging.info(f"Total da Consulta: {hours} horas = R$ {price}")
            else:
                raise InvalidDataException("A data de término deve ser superior à data de início")
        else:
            raise InvalidDataException("Data de início ou término não informada")
        return price
