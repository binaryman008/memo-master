from rest_framework import serializers
from users.models import UserModel

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ['password', 'email_id', 'first_name', 'last_name']
