import json
from uuid import UUID

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models.consultation_model import ConsultationModel


class ApiFinishConsultationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = "admin"
        cls.password = "teste123"
        User.objects.create_user(cls.user, "admin@test.com", password=cls.password)

    def test_api_start_ok(self):
        url = reverse("finish_consultation")
        data = {
            "consultation_id": "9c317dd5-a237-4e34-a059-96e7d2183aa9"
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ConsultationModel.objects.count(), 1)
        self.assertEqual(ConsultationModel.objects.get().physician_id, UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))

    def test_api_start_without_authentication(self):
        url = reverse("start_consultation")
        data = {
            "physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
            "patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e"
        }
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_start_empty_data(self):
        url = reverse("start_consultation")
        data = {
            "physician_id": "",
            "patient_id": ""
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type='text/plain')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_start_twice(self):
        url = reverse("start_consultation")
        data = {
            "physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
            "patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e"
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)