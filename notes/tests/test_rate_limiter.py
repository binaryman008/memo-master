from rest_framework.test import APITestCase, APIClient
from django.test import TestCase, RequestFactory
from django.http import HttpResponseForbidden
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from notes.api_views import NotesSearchAPIView  # Import your actual view function

class RateLimiterTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='testpassword',
        )
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.token = refresh.access_token

        # Set the token in the Authorization header for future requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_rate_limiter_allowed(self):
        # Create multiple requests within the rate limit
        for _ in range(5):
            response = self.client.get('http://localhost:8000/api/notes/search/?q=*')
            self.assertEqual(response.status_code, 200)

    def test_rate_limiter_exceeded(self):
        response = self.client.get('http://localhost:8000/api/notes/search/?q=*')
        # response = NotesSearchAPIView.as_view()(request)
        self.assertEqual(response.status_code, 403)