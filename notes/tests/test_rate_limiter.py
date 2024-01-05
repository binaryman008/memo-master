from rest_framework.test import APITestCase, APIClient
from django.test import TestCase, RequestFactory
from django.http import HttpResponseForbidden
from datetime import timedelta
from notes.api_views import NotesSearchAPIView  # Import your actual view function

class RateLimiterTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_rate_limiter_allowed(self):
        # Create multiple requests within the rate limit
        for _ in range(5):
            request = self.factory.get('http://localhost:8000')
            response = NotesSearchAPIView.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_rate_limiter_exceeded(self):
        request = self.factory.get('http://localhost:8000')
        response = NotesSearchAPIView.as_view()(request)
        self.assertEqual(response.status_code, 403)