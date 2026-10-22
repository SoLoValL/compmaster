from django.db import models

class DeviceType(models.Model):
    name = models.CharField('Тип устройства', max_length=100)  # Ноутбук, ПК, Моноблок...
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField('Услуга', max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price_from = models.DecimalField('Цена от', max_digits=8, decimal_places=2)
    device_types = models.ManyToManyField(DeviceType, related_name='services', blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
