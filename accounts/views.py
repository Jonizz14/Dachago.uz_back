from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            },
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
