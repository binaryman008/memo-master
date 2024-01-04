from django.urls import path, include

from notes.api_views import NotesLCView, NotesRUDView, NotesSearchAPIView


urlpatterns = [
    path("", NotesLCView.as_view(), name="notes_lc"),
    path("/<uuid:id>/", NotesRUDView.as_view(), name="notes_rud"),
    path('/search/', NotesSearchAPIView.as_view(), name='notes_search'),
]