from django.contrib import admin
from .models import User, MasterProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_master', 'phone']
    list_filter = ['is_master', 'is_active']
    search_fields = ['username', 'email', 'phone']


@admin.register(MasterProfile)
class MasterProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'is_available']
    list_filter = ['is_available']
    fields = ['user', 'photo', 'bio', 'skills', 'rating', 'is_available']
