from rest_framework import serializers
from .models import CalculatorCategory, CalculatorOption


class CalculatorOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorOption
        fields = ['id', 'name', 'extra_price', 'is_active']


class CalculatorCategorySerializer(serializers.ModelSerializer):
    options = CalculatorOptionSerializer(many=True, read_only=True)

    class Meta:
        model = CalculatorCategory
        fields = ['id', 'name', 'slug', 'base_price', 'options', 'is_active', 'order']
        read_only_fields = ['id', 'order']
