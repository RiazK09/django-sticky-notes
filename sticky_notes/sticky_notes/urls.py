# Import Django's admin site.
from django.contrib import admin

# Import path to create routes and include to connect
# the notes app routes to the main project.
from django.urls import include, path


# These are the main URL routes for the whole project.
urlpatterns = [
    # Django's built-in admin page.
    path("admin/", admin.site.urls),

    # Use all the URL routes from the notes app.
    path("", include("notes.urls")),
]
