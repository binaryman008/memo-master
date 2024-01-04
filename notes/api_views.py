from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from notes.serializers import NotesSerializer
from notes.models import NotesModel
from django_elasticsearch_dsl.search import Search
from notes.serializers import NotesSearchSerializer
from notes.models import NotesModel


class NotesLCView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        # Return only the notes created by the requesting user
        return NotesModel.objects.filter(author=self.request.user)
    

class NotesRUDView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    queryset = NotesModel.objects
    lookup_field = "id"


class NotesSearchAPIView(ListAPIView):
    serializer_class = NotesSerializer  # Replace with your serializer
    search_serializer_class = NotesSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        notes_search = Search(index='notes').query("multi_match", query=query, fields=['title', 'content'])
        notes = notes_search.execute()
        note_ids = [note.meta.id for note in notes]
        return NotesModel.objects.filter(id__in=note_ids)