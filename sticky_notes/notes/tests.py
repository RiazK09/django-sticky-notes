# Django's TestCase class provides tools for testing the application.
# It also creates a temporary database so that the real database
# and the user's saved notes are not changed during testing.
from django.test import TestCase

# Django's reverse function finds a page URL using its URL name.
# This avoids writing fixed URL paths directly inside the tests.
from django.urls import reverse

# Import the Note model so that test notes can be created,
# saved and checked inside the temporary test database.
from .models import Note


class NoteModelTests(TestCase):
    """Tests that check whether the Note model works correctly."""

    def setUp(self):
        # Create a fresh test note before each model test runs.
        # This gives every model test its own note to work with.
        self.note = Note.objects.create(
            title="Website Design",
            content="Complete the homepage layout.",
        )

    # Test 1: Check that the note title is saved correctly.
    def test_note_has_correct_title(self):
        # Compare the saved title with the title that was entered.
        self.assertEqual(self.note.title, "Website Design")

    # Test 2: Check that the note content is saved correctly.
    def test_note_has_correct_content(self):
        # Compare the saved content with the content that was entered.
        self.assertEqual(
            self.note.content,
            "Complete the homepage layout.",
        )

    # Test 3: Check how the note is displayed as text.
    def test_note_string_representation(self):
        # The Note model's __str__ method should return the note title.
        # This makes the note easier to recognise in places such as
        # the Django admin area or Python shell.
        self.assertEqual(str(self.note), "Website Design")


class NoteViewTests(TestCase):
    """Tests that check whether the sticky notes pages work correctly."""

    def setUp(self):
        # Create a fresh test note before each view test runs.
        # The note is used when testing the list and detail pages.
        self.note = Note.objects.create(
            title="Email Campaign",
            content="Prepare the June newsletter.",
        )

    # Test 4: Check that the note list page works correctly.
    def test_note_list_view(self):
        # self.client acts like a test web browser.
        # The get() method opens the page that displays all notes.
        response = self.client.get(reverse("note_list"))

        # A status code of 200 means that the page loaded successfully.
        self.assertEqual(response.status_code, 200)

        # Check that the title of the saved test note appears
        # somewhere on the note list page.
        self.assertContains(response, "Email Campaign")

        # Check that Django used the correct HTML template
        # when displaying the note list page.
        self.assertTemplateUsed(response, "notes/note_list.html")

    # Test 5: Check that the note detail page works correctly.
    def test_note_detail_view(self):
        # Open the detail page for the note created in setUp().
        # The note ID tells Django which specific note to display.
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )

        # A status code of 200 means that the page loaded successfully.
        self.assertEqual(response.status_code, 200)

        # Check that both the note title and note content
        # appear on the detail page.
        self.assertContains(response, "Email Campaign")
        self.assertContains(response, "Prepare the June newsletter.")

        # Check that Django used the correct HTML template
        # when displaying the note detail page.
        self.assertTemplateUsed(response, "notes/note_detail.html")

    # Test 6: Check that a new note can be created.
    def test_note_create_view(self):
        # self.client.post() acts like a user completing and
        # submitting the form used to create a new note.
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "Website Migration",
                "content": "Move the client website to the new server.",
            },
        )

        # A status code of 302 means that Django redirected the user
        # after the new note was created successfully.
        self.assertEqual(response.status_code, 302)

        # Search the temporary database for the newly created note.
        # exists() returns True if a matching note was saved.
        self.assertTrue(
            Note.objects.filter(title="Website Migration").exists()
        )

    # Test 7: Check that an existing note can be updated.
    def test_note_update_view(self):
        # Submit changed note information to the update page.
        # The note ID tells Django which note must be edited.
        response = self.client.post(
            reverse("note_update", args=[self.note.id]),
            {
                "title": "Updated Email Campaign",
                "content": "Send the revised June newsletter.",
            },
        )

        # A status code of 302 means Django redirected the user
        # after the note was updated successfully.
        self.assertEqual(response.status_code, 302)

        # Reload the note from the temporary test database.
        # This makes sure we check the latest saved information.
        self.note.refresh_from_db()

        # Check that the title and content were both updated.
        self.assertEqual(
            self.note.title,
            "Updated Email Campaign",
        )
        self.assertEqual(
            self.note.content,
            "Send the revised June newsletter.",
        )

    # Test 8: Check that an existing note can be deleted.
    def test_note_delete_view(self):
        # Submit a request to delete the note created in setUp().
        # The note ID tells Django which note must be removed.
        response = self.client.post(
            reverse("note_delete", args=[self.note.id])
        )

        # A status code of 302 means Django redirected the user
        # after the note was deleted successfully.
        self.assertEqual(response.status_code, 302)

        # Check that the deleted note no longer exists
        # in the temporary test database.
        self.assertFalse(
            Note.objects.filter(id=self.note.id).exists()
        )
