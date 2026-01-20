from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from .models import Product, Blog
from .serializers import ProductSerializer, BlogSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class UserViewSet(viewsets.ModelViewSet):
    """
    Userlarni ko'rish va o'chirish uchun ViewSet.
    Faqat adminlar o'chira oladi.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-published_date')
    serializer_class = BlogSerializer
