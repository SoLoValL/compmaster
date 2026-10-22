from django.contrib import admin
from .models import WorkExample


@admin.register(WorkExample)
class WorkExampleAdmin(admin.ModelAdmin):
    list_display = ['title', 'device_type', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
