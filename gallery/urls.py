from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BlogViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
