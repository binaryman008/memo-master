import logging
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.views import APIView
from django_elasticsearch_dsl.search import Search
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from notes.serializers import NotesSerializer
from notes.models import NotesModel
from users.models import UserModel
from notes.serializers import NotesSearchSerializer
from notes.models import NotesModel
from notes.rate_limiter import rate_limiter

logger = logging.getLogger('my_logger')

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

# Check if the index exists
if not es.indices.exists(index='notes'):
    # Create the index if it doesn't exist
    es.indices.create(index='notes')


# @method_decorator(rate_limiter, name='dispatch')
class NotesLCView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        # Return only the notes created by the requesting user
        return NotesModel.objects.filter(author=self.request.user)
    

@method_decorator(rate_limiter, name='dispatch')
class NotesRUDView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    queryset = NotesModel.objects
    lookup_field = "id"


# @method_decorator(rate_limiter, name='dispatch')
class ShareNotesAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        try:
            # return Response({})
            user_id = UserModel.objects.get(id=id)
            notes_id = json.loads(request.body)["notes_id"]
            notes = NotesModel.objects.get(id=notes_id)
            NotesModel.objects.create(author=user_id,title = notes.title,content=notes.content)
            return Response({"msg":"Note Shared Succesfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"msg":False, "error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(rate_limiter, name='dispatch')
class NotesSearchAPIView(ListAPIView):
    serializer_class = NotesSerializer  # Replace with your serializer
    search_serializer_class = NotesSearchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            query = self.request.query_params.get('q', '')
            notes_search = Search(index='notes').query("multi_match", query=query, fields=['title', 'content'])
            notes = notes_search.execute()
            note_ids = [note.meta.id for note in notes]
            return NotesModel.objects.filter(id__in=note_ids)
        except:
            return Response({
                "success":False,
                "msg": "Server Error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)