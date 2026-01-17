from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BlogViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
