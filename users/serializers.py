from rest_framework import serializers
from users.models import UserModel

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ['password', 'first_name', 'last_name', 'email', 'id']

    def create(self, validated_data):
        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)