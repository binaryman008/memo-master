# myapp/tests/test_models.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from notes.models import NotesModel

class NotesModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )

        # Create a NotesModel instance
        self.note = NotesModel.objects.create(
            author=self.user,
            title='Test Note Title',
            content='Test Note Content'
        )

    def test_notes_model_fields(self):
        # Test the fields of the NotesModel instance
        self.assertEqual(str(self.note.title), 'Test Note Title')
        self.assertEqual(str(self.note.content), 'Test Note Content')

    def test_notes_model_author(self):
        # Test the author field of the NotesModel instance
        self.assertEqual(self.note.author, self.user)

    def test_notes_model_created_modified(self):
        # Test the created_on and modified_on fields
        self.assertIsNotNone(self.note.created_on)
        self.assertIsNotNone(self.note.modified_on)
