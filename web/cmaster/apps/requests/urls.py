from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RepairRequestViewSet

router = DefaultRouter()
router.register(r'', RepairRequestViewSet, basename='repair-request')

urlpatterns = [
    path('', include(router.urls)),
]
