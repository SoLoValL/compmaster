from django.contrib import admin
from .models import SiteSettings, SliderItem


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'seo_title']
    fields = ['phone', 'address', 'email', 'seo_title', 'seo_description']


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    fields = ['title', 'text', 'image', 'order', 'is_active']
