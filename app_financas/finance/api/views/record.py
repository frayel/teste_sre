import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.converter.payment_converter import PaymentConverter
from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.payment_service import PaymentService


class RecordView(APIView):
    """ View para registro financeiro de uma consulta
        url: /app/finance/record/ """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    service = PaymentService()
    converter = PaymentConverter()

    def post(self, request):
        logging.info(f"API finance.record acessada por {request.user.username}")

        try:
            dto = self.converter.from_text(request.body)
            payment_dto = self.service.record(dto)

        except InvalidDataException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            logging.exception("Ocorreu uma operação inválida ao registrar o pagamento.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Pagamento da consulta {payment_dto.appointment_id} Registrado!", status=status.HTTP_201_CREATED)

