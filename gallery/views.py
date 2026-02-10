from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Product, Blog, Contact
from .serializers import ProductSerializer, BlogSerializer, ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products"""
        featured = Product.objects.filter()[:6]
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset
    
    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Get latest blog posts"""
        latest = Blog.objects.order_by('-published_date')[:10]
        serializer = self.get_serializer(latest, many=True)
        return Response(serializer.data)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        queryset = Contact.objects.all()
        return queryset
    
    @action(detail=False, methods=['post'])
    def submit(self, request):
        """Submit a contact form"""
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Ваше сообщение отправлено! / Xabaringiz yuborildi!'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        """Mark contact as read"""
        contact = self.get_object()
        contact.is_read = True
        contact.save()
        serializer = self.get_serializer(contact)
        return Response(serializer.data)
