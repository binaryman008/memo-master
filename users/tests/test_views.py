from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import UserModel
from django.contrib.auth import get_user_model

class RegisterApiIntegrationTest(APITestCase):
    def setUp(self):
        # Define test user data
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
        }

    def test_register_user_integration(self):
        response = self.client.post(reverse('signup'), data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(UserModel.objects.filter(email=self.user_data['email']).exists())


class LoginViewIntegrationTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User',
        )

        # Define test login data
        self.login_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }

    def test_login_user_integration(self):
        # Make a POST request to the login API
        response = self.client.post(reverse('login'), data=self.login_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
