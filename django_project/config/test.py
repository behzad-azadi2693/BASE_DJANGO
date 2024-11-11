from django.urls import reverse
from rest_framework.test import APITestCase

class SchemaGenerationTestCase(APITestCase):
    def test_schema_generation(self):
        url = reverse('schema')  # 'schema' is the name of the SpectacularAPIView
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('openapi', response.data)  # Check if 'openapi' key is in the response
