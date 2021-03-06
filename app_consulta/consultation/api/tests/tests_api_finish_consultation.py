import json
from uuid import UUID

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from api.models.consultation_model import ConsultationModel


class ApiFinishConsultationTest(TestCase):

    user: str
    password: str

    @classmethod
    def setUpTestData(cls):
        cls.user = settings.API_USERNAME
        cls.password = settings.API_PASSWORD
        User.objects.create_user(cls.user, "admin@test.com", password=cls.password)
        consultation = ConsultationModel(
            id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"),
            start_date=timezone.now(),
            end_date=None,
            physician_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"),
            patient_id=UUID("86158d46-ce33-4e3d-9822-462bbff5782e"),
            price=None,
        )
        consultation.save()

    def test_api_finish_ok(self):
        url = reverse("finish_consultation")
        data = {
            "consultation_id": "9c317dd5-a237-4e34-a059-96e7d2183aa9"
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.put(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        consultation = ConsultationModel.objects.filter(id="9c317dd5-a237-4e34-a059-96e7d2183aa9").first()
        self.assertIsNotNone(consultation.end_date)
        self.assertIsNotNone(consultation.price)

    def test_api_finish_without_authentication(self):
        url = reverse("finish_consultation")
        data = {
            "consultation_id": "9c317dd5-a237-4e34-a059-96e7d2183aa9"
        }
        response = self.client.put(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_finish_empty_data(self):
        url = reverse("finish_consultation")
        data = {
            "consultation_id": ""
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.put(url, json.dumps(data), content_type='text/plain')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_start_empty_keys(self):
        url = reverse("finish_consultation")
        data = {}
        self.client.login(username=self.user, password=self.password)
        response = self.client.put(url, json.dumps(data), content_type='text/plain')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_finish_twice(self):
        url = reverse("finish_consultation")
        data = {
            "consultation_id": "9c317dd5-a237-4e34-a059-96e7d2183aa9"
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.put(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        response = self.client.put(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

