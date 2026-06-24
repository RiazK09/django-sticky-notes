# Import Django's model tools so we can create database tables
# using Python classes.
from django.db import models


# This class represents one sticky note in the database.
class Note(models.Model):

    # Store the note heading.
    # max_length limits the title to 200 characters.
    title = models.CharField(max_length=200)

    # Store the main note text.
    # TextField is used because the content may be longer.
    content = models.TextField()

    # This controls how each note is shown in places
    # like the Django admin area.
    def __str__(self):
        return self.title
