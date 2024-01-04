from rest_framework import serializers
from notes.models import NotesModel


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = ['id', 'title', 'content', 'author', 'created_on', 'modified_on']
        read_only_fields = ['author', 'created_on', 'modified_on']

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        notes = NotesModel.objects.create(**validated_data)
        return notes
    

class NotesSearchSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=255, required=True, help_text='Search query')

