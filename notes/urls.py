from django.urls import path, include

from notes.api_views import NotesLCView


urlpatterns = [
    path("", NotesLCView.as_view(), name="notes_lc"),
]