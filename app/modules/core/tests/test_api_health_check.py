from rest_framework import status
from rest_framework.reverse import reverse

from modules.core.tests.base import BaseAPITestCase


class ApiHealthCheckTestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.api_health_check = reverse("api-health-check")

    def test_api_health_check(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.api_health_check)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")
