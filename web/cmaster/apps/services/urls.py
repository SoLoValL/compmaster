from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceTypeViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'device-types', DeviceTypeViewSet, basename='device-type')
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]
