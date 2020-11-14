from rest_framework import status
from rest_framework.reverse import reverse

from modules.core.tests.base import BaseAPITestCase


class ErrorHandlersTestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_404_error_handler_check(self):
        response = self.client.get("/obviously-non-existing-uri/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
