from django.contrib import admin
from .models import CalculatorCategory, CalculatorOption


@admin.register(CalculatorCategory)
class CalculatorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(CalculatorOption)
class CalculatorOptionAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'extra_price', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
