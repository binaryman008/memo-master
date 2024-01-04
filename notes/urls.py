from django.urls import path, include

from notes.api_views import NotesLCView, NotesRUDView


urlpatterns = [
    path("", NotesLCView.as_view(), name="notes_lc"),
    path("/<uuid:id>/", NotesRUDView.as_view(), name="notes_rud"),
]