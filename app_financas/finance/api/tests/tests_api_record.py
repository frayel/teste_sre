import json
from uuid import UUID

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models.payment_model import PaymentModel


class ApiRecordTest(TestCase):

    user: str
    password: str

    @classmethod
    def setUpTestData(cls):
        cls.user = settings.API_USERNAME
        cls.password = settings.API_PASSWORD
        User.objects.create_user(cls.user, "admin@test.com", password=cls.password)

    def test_api_record_ok(self):
        url = reverse("record")
        data = {
            "appointment_id": "84ab6121-c4a8-4684-8cc2-b03024ec0f1d",
            "total_price": "400.00"
        }

        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PaymentModel.objects.count(), 1)
        self.assertEqual(PaymentModel.objects.get().appointment_id, UUID("84ab6121-c4a8-4684-8cc2-b03024ec0f1d"))

    def test_api_start_without_authentication(self):
        url = reverse("record")
        data = {
            "appointment_id": "84ab6121-c4a8-4684-8cc2-b03024ec0f1d",
            "total_price": "400.00"
        }
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_start_empty_data(self):
        url = reverse("record")
        data = {
            "appointment_id": "",
            "total_price": ""
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type='text/plain')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_start_empty_keys(self):
        url = reverse("record")
        data = {}
        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type='text/plain')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_start_twice(self):
        url = reverse("record")
        data = {
            "appointment_id": "84ab6121-c4a8-4684-8cc2-b03024ec0f1d",
            "total_price": "400.00"
        }
        self.client.login(username=self.user, password=self.password)
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(url, json.dumps(data), content_type="text/plain")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

