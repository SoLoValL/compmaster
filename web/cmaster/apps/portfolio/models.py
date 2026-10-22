from django.db import models
from apps.services.models import DeviceType

class WorkExample(models.Model):
    title = models.CharField(max_length=200)
    device_type = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image_before = models.ImageField(upload_to='portfolio/before/', blank=True)
    image_after = models.ImageField(upload_to='portfolio/after/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'

    def __str__(self):
        return self.title
