# Import Django's form tools so we can create a form
# connected to our Note model.
from django import forms

# Import the Note model so the form knows which
# database fields it should use.
from .models import Note


# This form will be used to create and edit sticky notes.
class NoteForm(forms.ModelForm):

    # The Meta class tells Django which model and fields
    # should be included in the form.
    class Meta:
        model = Note
        fields = ["title", "content"]
