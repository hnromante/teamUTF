from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from rest_framework.generics import (
    ListAPIView
)

from rest_framework.permissions import (
    AllowAny
)

from .serializers import(
    UserDetailSerializer
)

User = get_user_model()

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer    
