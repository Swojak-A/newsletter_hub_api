import logging

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory, APIClient, APITestCase


class BaseAPITestCase(APITestCase):
    client_class = APIClient

    def setUp(self):
        logging.disable(logging.CRITICAL)
        User = get_user_model()
        self.user_password = "pass1234"
        self.user = User.objects.create_user(
            username="user", password=self.user_password
        )
        self.factory = APIRequestFactory()
        super().setUp()

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def assertResponseMethodNotAllowed(self, response: Response) -> None:
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data["code"], "method_not_allowed")
