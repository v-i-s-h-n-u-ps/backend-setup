from rest_framework import serializers

from user.models import *


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile', 'github_url', 'fcm_token', 'role']


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class RevokeTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class SignUpSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    mobile = serializers.CharField()
    password = serializers.CharField()
    role = serializers.CharField()
    github_url = serializers.CharField(allow_blank=True)
