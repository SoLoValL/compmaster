from rest_framework import serializers
from .models import Service, DeviceType


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ['id', 'name', 'slug']


class ServiceSerializer(serializers.ModelSerializer):
    device_types = DeviceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'description',
            'price_from', 'device_types', 'is_active', 'order'
        ]
        read_only_fields = ['id', 'order']
