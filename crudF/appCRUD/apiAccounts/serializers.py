from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer
)
from rest_framework import serializers

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name'
        ]

