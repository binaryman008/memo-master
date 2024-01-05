# users/tests/test_models.py
from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        manager = User.objects
        email = 'testuser@example.com'
        password = 'testpassword'
        user = manager.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        manager = User.objects
        email = 'admin@example.com'
        password = 'adminpassword'
        superuser = manager.create_superuser(email, password)

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class UserModelTest(TestCase):
    def test_user_model_fields(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='John',
            last_name='Doe'
        )

        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'testuser@example.com')

