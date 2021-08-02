import logging

from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.dto.finish_consultation_parameter_dto import FinishConsultationParameterDto
from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.finish_consultation_service import FinishConsultationService


class FinishConsutationView(APIView):
    """ View para término de uma consulta
        url: /app/consultation/finish/ """

    # Definição para autenticação
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Classe de serviço para término da consulta
    finish = FinishConsultationService()

    def post(self, request):
        logging.info(f"API consultation.finish acessada por {request.user.username}")
        try:
            # Converte o texto de entrada em dto
            input_dto = FinishConsultationParameterDto().from_dict(JSONParser().parse(request)).validate()
            # Chama o serviço para iniciar a consulta
            consultation_dto = self.finish.end(input_dto)

        except InvalidDataException as e:
            # Responde com o status 400 no caso de haver dados inválidos na entrada
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            # Responde com status 400 no caso de ocorrer um erro no serviço
            logging.exception("Ocorreu uma operação inválida ao encerrar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(consultation_dto.__dict__, status=status.HTTP_202_ACCEPTED)

