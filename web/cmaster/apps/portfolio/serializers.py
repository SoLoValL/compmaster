from rest_framework import serializers
from .models import WorkExample
from apps.services.serializers import DeviceTypeSerializer


class WorkExampleSerializer(serializers.ModelSerializer):
    device_type = DeviceTypeSerializer(read_only=True)

    class Meta:
        model = WorkExample
        fields = [
            'id', 'title', 'device_type', 'description',
            'image_before', 'image_after', 'created_at'
        ]
        read_only_fields = ['created_at']

    # TODO (студенты): валидация — размер изображения не более 5 МБ
    def validate_image_before(self, value):
        max_size = 5 * 1024 * 1024  # 5 МБ
        if value.size > max_size:
            raise serializers.ValidationError(
                'Размер изображения не должен превышать 5 МБ.'
            )
        return value

    def validate_image_after(self, value):
        max_size = 5 * 1024 * 1024  # 5 МБ
        if value.size > max_size:
            raise serializers.ValidationError(
                'Размер изображения не должен превышать 5 МБ.'
            )
        return value
