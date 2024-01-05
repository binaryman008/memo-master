from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from notes.models import NotesModel
from users.models import UserModel

class NotesLCViewTest(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='testpassword',
        )

        # Set up the client
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.token = refresh.access_token

        # Set the token in the Authorization header for future requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_list_notes(self):
        NotesModel.objects.create(author=self.user, title='Note 1', content='Content 1')
        NotesModel.objects.create(author=self.user, title='Note 2', content='Content 2')
        response = self.client.get('http://localhost:8000/api/notes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)


    def test_create_note(self):
        data = {'title': 'New Note', 'content': 'New Content'}
        response = self.client.post('http://localhost:8000/api/notes', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NotesModel.objects.filter(author=self.user).count(), 1)


class ShareNotesAPIViewIntegrationTest(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword',
        )

        self.user2 = get_user_model().objects.create_user(
            email='testuser2@example.com',
            password='testpassword',
        )

        # Create a note for sharing
        self.note = NotesModel.objects.create(
            author=self.user,
            title='Test Note',
            content='Test Content',
        )
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.token = refresh.access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
