import re

from rest_framework import serializers
from .models import RepairRequest
from apps.services.serializers import DeviceTypeSerializer, ServiceSerializer


class RepairRequestCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для СОЗДАНИЯ заявки с фронтенда.
    Принимает только id связанных объектов.
    """
    class Meta:
        model = RepairRequest
        fields = [
            'id', 'name', 'phone', 'device_type', 'service',
            'problem_description', 'address', 'is_pickup',
        ]

    def validate_phone(self, value):
        # Проверка формата: +7XXXXXXXXXX или 8XXXXXXXXXX (10 цифр после кода)
        cleaned = value.replace('+', '').replace(' ', '').replace('-', '')
        if not re.match(r'^7?\d{10}$', cleaned):
            raise serializers.ValidationError(
                'Телефон должен содержать код страны (7) и 10 цифр. '
                'Пример: +79991234567'
            )
        return value

    def validate_problem_description(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError(
                'Описание проблемы не может быть пустым.'
            )
        return value


class RepairRequestSerializer(serializers.ModelSerializer):
    """Сериализатор для ПОЛУЧЕНИЯ данных заявки."""
    device_type = DeviceTypeSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = RepairRequest
        fields = [
            'id', 'name', 'phone', 'device_type', 'service',
            'problem_description', 'address', 'is_pickup',
            'status', 'created_at'
        ]
        read_only_fields = ['status', 'created_at']
