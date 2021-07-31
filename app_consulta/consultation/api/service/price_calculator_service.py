import logging

from api.config.consultation_config import ConsultationConfig


class PriceCalculatorService:
    """ Calcula o preço de uma consulta """
    config = ConsultationConfig()

    def calculate(self, start_date, end_date):
        logging.info('Iniciando o cálculo de preços')
        tempo = end_date - start_date
        price = self.config.price * tempo
        return price
