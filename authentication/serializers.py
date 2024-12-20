from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email is already in use.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
