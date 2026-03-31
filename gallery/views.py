from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import (
    Product, Blog, Contact, Booking, Review, Activity,
    Employee, Payment, Service, Announcement, Settings
)
from .serializers import (
    ProductSerializer, BlogSerializer, ContactSerializer, 
    BookingSerializer, ReviewSerializer, ActivitySerializer, UserSerializer,
    EmployeeSerializer, PaymentSerializer, ServiceSerializer, 
    AnnouncementSerializer, SettingsSerializer
)
from django.contrib.auth.models import User


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('availability', 'reviews', 'bookings')
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Add basic filtering logic if needed (e.g. by category or status)
        category = self.request.query_params.get('category')
        status_val = self.request.query_params.get('status')
        if category:
            queryset = queryset.filter(category=category)
        if status_val:
            queryset = queryset.filter(status=status_val)
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products"""
        featured = self.get_queryset()[:6]
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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def stats(self, request):
        return Response({
            'total_users': User.objects.count(),
            'vip_users': User.objects.filter(is_staff=True).count(), # Placeholder for VIP
            'active_users': User.objects.filter(is_active=True).count(),
        })


class DashboardViewSet(viewsets.ViewSet):
    """
    Specially crafted ViewSet for Admin Dashboard
    """
    def list(self, request):
        from django.db.models import Sum, Avg
        
        # Stats Cards
        total_cottages = Product.objects.count()
        total_users = User.objects.count()
        # Total Revenue
        total_revenue = Booking.objects.filter(status='confirmed').aggregate(Sum('price'))['price__sum'] or 0
        avg_rating = Review.objects.aggregate(Avg('rating'))['rating__avg'] or 0
        
        # Recent Bookings (Match keys in AdminDashboard.jsx)
        recent_bookings = Booking.objects.select_related('product', 'user').order_by('-created_at')[:5]
        bookings_data = []
        for b in recent_bookings:
            bookings_data.append({
                'key': str(b.id),
                'name': b.product.title,
                'user': b.user_name,
                'date': b.date.strftime('%Y-%m-%d'),
                'status': b.status,
                'price': float(b.price)
            })
            
        # Top Performing Cottages (Match keys in AdminDashboard.jsx)
        top_cottages = Product.objects.all()[:5]
        top_cottages_data = []
        for p in top_cottages:
            top_cottages_data.append({
                'name': p.title,
                'bookings': p.bookings.count(),
                'revenue': float(p.bookings.filter(status='confirmed').aggregate(Sum('price'))['price__sum'] or 0),
                'rating': round(p.reviews.aggregate(Avg('rating'))['rating__avg'] or 0, 1)
            })
            
        # Recent Activities (Match keys in AdminDashboard.jsx)
        recent_activities = Activity.objects.order_by('-created_at')[:10]
        activities_data = []
        for a in recent_activities:
            activities_data.append({
                'title': a.title,
                'description': a.description,
                'icon_type': a.icon_type, # Icon mapping handled in frontend
                'time': a.created_at.strftime('%Y-%m-%d %H:%M')
            })
            
        # Monthly Progress
        progress_data = [
            {'title': 'Target', 'percent': 78, 'status': 'active'},
            {'title': 'User Registration', 'percent': 65, 'status': 'active'},
            {'title': 'Customer Satisfaction', 'percent': 92, 'status': 'success'},
        ]
        
        return Response({
            'stats': [
                {'title': 'Total Cottages', 'value': total_cottages, 'color': '#1890ff'},
                {'title': 'Total Users', 'value': total_users, 'color': '#52c41a'},
                {'title': 'Total Revenue', 'value': float(total_revenue), 'color': '#faad14', 'suffix': '$'},
                {'title': 'Average Rating', 'value': round(avg_rating, 1), 'color': '#f5222d', 'precision': 1},
            ],
            'recentBookings': bookings_data,
            'topCottages': top_cottages_data,
            'recentActivities': activities_data,
            'progressData': progress_data
        })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().select_related('product', 'user')
    serializer_class = ReviewSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        return Payment.objects.order_by('-date')


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().select_related('product', 'user')
    serializer_class = BookingSerializer


class SettingsViewSet(viewsets.ViewSet):
    """
    Settings are usually a single record.
    """
    def list(self, request):
        settings, created = Settings.objects.get_or_create(id=1)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)

    def create(self, request):
        settings, created = Settings.objects.get_or_create(id=1)
        serializer = SettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
