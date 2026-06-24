# Import Django helper functions used to display pages,
# find notes, and move the user to another page.
from django.shortcuts import get_object_or_404, redirect, render

# Import the form used to create and edit notes.
from .forms import NoteForm

# Import the Note model so we can work with saved notes.
from .models import Note


# Display all saved notes on the main page.
def note_list(request):
    notes = Note.objects.all()

    return render(
        request,
        "notes/note_list.html",
        {"notes": notes},
    )


# Display the full details of one note.
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(
        request,
        "notes/note_detail.html",
        {"note": note},
    )


# Display a blank form and save a new note.
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(
        request,
        "notes/note_form.html",
        {"form": form},
    )


# Display an existing note in the form and save any changes.
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "notes/note_form.html",
        {"form": form},
    )


# Ask the user to confirm before deleting a note.
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note},
    )
