from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Service, DeviceType
from .serializers import ServiceSerializer, DeviceTypeSerializer


class DeviceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Типы устройств — только чтение."""
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    lookup_field = 'slug'


class ServiceViewSet(viewsets.ModelViewSet):
    """Услуги — CRUD, но менять может только авторизованный."""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
