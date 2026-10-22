from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    customer_name_display = serializers.CharField(
        source='customer_name', read_only=True
    )

    class Meta:
        model = Review
        fields = [
            'id', 'service', 'customer_name', 'customer',
            'rating', 'text', 'is_published', 'created_at'
        ]
        read_only_fields = ['created_at']
