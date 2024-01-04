from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from notes.models import NotesModel
from notes.serializers import NotesSerializer

class NotesSerializerTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            email_id='testuser@example.com',
            password='testpassword'
        )

    def test_create_method_sets_author(self):
        # Create a serializer instance with some data
        serializer = NotesSerializer(
            data={'title': 'Test Title', 'content': 'Test Content'},
            context={'request': self._create_fake_request()}
        )

        # Validate the serializer and check if the author is set
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()

        # Check if the author is set correctly
        self.assertEqual(instance.author, self.user)

    def _create_fake_request(self):
        """
        Create a fake request object for testing purposes.
        """
        request = self.client.request().wsgi_request
        request.user = self.user
        return request