import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.finish_consultation_service import FinishConsultationService
from api.converter.finish_consultation_converter import FinishConsultationConverter


class FinishConsutationView(APIView):
    """ View para término de uma consulta
        url: /app/consultation/finish/ """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    finish = FinishConsultationService()
    converter = FinishConsultationConverter()

    def post(self, request):
        logging.info(f"API consultation.finish acessada por {request.user.username}")
        try:
            dto = self.converter.from_text(request.body)
            consultation_dto = self.finish.end(dto)

        except InvalidDataException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            logging.exception("Ocorreu uma operação inválida ao encerrar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Consulta {consultation_dto.id} Encerrada às {consultation_dto.end_date}", status=status.HTTP_202_ACCEPTED)

