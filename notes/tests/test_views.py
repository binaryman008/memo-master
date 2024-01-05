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
        # Create some notes for the user
        NotesModel.objects.create(author=self.user, title='Note 1', content='Content 1')
        NotesModel.objects.create(author=self.user, title='Note 2', content='Content 2')

        # Make a GET request to the API endpoint
        response = self.client.get('http://localhost:8000/api/notes')

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the correct number of notes is returned for the user
        self.assertEqual(len(response.data["results"]), 2)

        # Optionally, you can add more specific assertions based on your serializer and expected data

    def test_create_note(self):
        # Make a POST request to create a new note
        data = {'title': 'New Note', 'content': 'New Content'}
        response = self.client.post('http://localhost:8000/api/notes', data)

        # Check that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the note is created for the correct user
        self.assertEqual(NotesModel.objects.filter(author=self.user).count(), 1)

        # Optionally, you can add more specific assertions based on your serializer and expected data


# class ShareNotesAPIViewIntegrationTest(APITestCase):
#     def setUp(self):
#         # Create a user for authentication
#         self.user = get_user_model().objects.create_user(
#             email='testuser@example.com',
#             password='testpassword',
#         )

#         self.user2 = get_user_model().objects.create_user(
#             email='testuser2@example.com',
#             password='testpassword',
#         )

#         # Create a note for sharing
#         self.note = NotesModel.objects.create(
#             author=self.user,
#             title='Test Note',
#             content='Test Content',
#         )
#         self.client = APIClient()
#         refresh = RefreshToken.for_user(self.user)
#         # Obtain a JWT token for the user
#         # response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
#         # print(refresh.access_token)
#         self.token = refresh.access_token

#         # Set the token in the Authorization header for future requests
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

#     def test_share_note_integration(self):

#         print(f'http://localhost:8000/api/notes/{str(self.user2.id)}/share', "   ", str(self.note.id))
#         note_id = str(self.note.id)
#         user2_id = str(self.user2.id)
#         data={"notes_id":note_id}
#         # Share the note
#         print(self.client.credentials)
#         response = self.client.post(f'http://localhost:8000/api/notes/{user2_id}/share', data=data)
#         print(response)

#         # Check that the response status code is 201 Created
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
