
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User


class RegisterView(generics.CreateAPIView):
    """
    API view for user registeration
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
