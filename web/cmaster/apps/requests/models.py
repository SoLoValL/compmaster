from django.db import models
from apps.services.models import Service, DeviceType

class RepairRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('diagnostics', 'Диагностика'),
        ('repair', 'В ремонте'),
        ('ready', 'Готово'),
        ('issued', 'Выдано'),
        ('cancelled', 'Отменено'),
    ]

    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    device_type = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    problem_description = models.TextField('Описание проблемы')
    address = models.CharField('Адрес', max_length=255, blank=True)
    is_pickup = models.BooleanField('Нужен выезд мастера', default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на ремонт'
        verbose_name_plural = 'Заявки на ремонт'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.phone}'
