from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteTests(TestCase):
    def setUp(self):
        # Create a sample note for testing
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test content"
        )

    def test_note_content(self):
        """Check if the note was created correctly in the DB"""
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test content")

    def test_list_view(self):
        """Check if the homepage loads and shows our note"""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_create_note(self):
        """Test if a user can successfully submit a new note"""
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302) # Should redirect after save
        self.assertEqual(Note.objects.count(), 2)