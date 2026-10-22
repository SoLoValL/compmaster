from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
