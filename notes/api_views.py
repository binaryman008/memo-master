from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from notes.serializers import NotesSerializer
from notes.models import NotesModel


class NotesLCView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    
    def get_queryset(self):
        # Return only the notes created by the requesting user
        return NotesModel.objects.filter(author=self.request.user)
    

class NotesRUDView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    queryset = NotesModel.objects
    lookup_field = "id"