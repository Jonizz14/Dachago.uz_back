from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, BlogViewSet, ContactViewSet, 
    UserViewSet, DashboardViewSet, EmployeeViewSet,
    PaymentViewSet, ServiceViewSet, AnnouncementViewSet,
    ReviewViewSet, SettingsViewSet, BookingViewSet
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'users', UserViewSet, basename='user')
router.register(r'dashboard', DashboardViewSet, basename='dashboard')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'settings', SettingsViewSet, basename='settings')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
