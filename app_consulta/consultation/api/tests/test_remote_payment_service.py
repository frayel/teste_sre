from unittest.mock import patch

from django.test import TestCase

from api.dto.pending_payment_dto import PendingPaymentDto
from api.service.remote.remote_payment_service import RemotePaymentService


class RemotePaymentServiceTest(TestCase):

    @patch('api.service.remote.remote_payment_service.requests.post')
    def test_send(self, mock_send):
        mock_send.return_value.status_code = 200
        service = RemotePaymentService()
        dto = PendingPaymentDto()
        result = service.send(dto)
        self.assertTrue(result)