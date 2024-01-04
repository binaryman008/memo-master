from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from notes.serializers import NotesSerializer


class NotesLCView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    