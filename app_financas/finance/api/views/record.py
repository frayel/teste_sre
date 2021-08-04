import logging

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.dto.payment_dto import PaymentDto
from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.payment_service import PaymentService


class RecordView(APIView):
    """ View para registro financeiro de uma consulta
        url: /app/finance/record/ """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Definição para autenticação
        self.authentication_classes = [SessionAuthentication, BasicAuthentication]
        self.permission_classes = [IsAuthenticated]

        # Classe de serviço para registro financeiro
        self.service = PaymentService()

    def post(self, request):
        logging.info(f"API finance.record acessada por {request.user.username}")

        try:
            # Converte a entrada em DTO
            input_dto = PaymentDto().from_dict(JSONParser().parse(request)).validate()
            # Chama o serviço para registrar o recebimento
            payment_dto = self.service.record(input_dto)

        except (InvalidDataException, ValidationError, InvalidOperationException) as e:
            # Responde com o status 400 no caso de existir dados inválidos no parametro
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Responde com status 400 e registra em log no caso de ocorrer um erro não especificado
            logging.exception("Ocorreu uma operação inválida ao registrar o pagamento.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(payment_dto.__dict__, status=status.HTTP_201_CREATED)
