from django.contrib.auth import authenticate, login
from rest_framework import serializers

from user_app.models import UserModel


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "username", "first_name", "last_name", "email","password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        return UserModel.objects.create_user(**validated_data)  # ** used to give key value pair


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        print(validated_data)
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        print(user)
        if not user:
            raise serializers.FieldDoesNotExist
        login(self.context.get('request'), user)
        return user
