# users/tests/test_serializers.py
from django.test import TestCase
from users.models import UserModel
from users.serializers import UserRegistrationSerializer, LoginSerializer

class UserRegistrationSerializerTest(TestCase):
    def test_create_user(self):
        data = {
            'password': 'testpassword',
            'email': 'testuser@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()

        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertTrue(user.check_password(data['password']))

class LoginSerializerTest(TestCase):
    def test_valid_login_data(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }

        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_login_data(self):
        data = {
            'email': 'testuser@example.com',
            'password': ''
        }

        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
