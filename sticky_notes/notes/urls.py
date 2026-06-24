# Import Django's path function so we can create URL routes.
from django.urls import path

# Import the views that each URL must open.
from . import views


# Each path connects a browser URL to a view function.
urlpatterns = [
    # Main page showing all notes.
    path("", views.note_list, name="note_list"),

    # Page showing one specific note.
    path("note/<int:pk>/", views.note_detail, name="note_detail"),

    # Page used to create a new note.
    path("note/new/", views.note_create, name="note_create"),

    # Page used to edit an existing note.
    path("note/<int:pk>/edit/", views.note_update, name="note_update"),

    # Page used to confirm and delete a note.
    path("note/<int:pk>/delete/", views.note_delete, name="note_delete"),
]
