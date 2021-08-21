import asyncio

from django.core.management.base import BaseCommand

from core.service.process_payment_service import ProcessPaymentService


class Command(BaseCommand):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ProcessPaymentService()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f'Iniciando Payment Process Consumer...'))
        while True:
            self.service.process()
        self.stdout.write(self.style.SUCCESS(f'Payment Process Consumer Encerrado...'))

