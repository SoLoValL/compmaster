from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Review(models.Model):
    """Отзыв клиента."""
    service = models.CharField('Услуга', max_length=200, blank=True)

    customer_name = models.CharField('Имя клиента', max_length=100, blank=True)
    # Можно привязать к пользователю, если он авторизован
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='reviews', verbose_name='Клиент'
    )

    rating = models.PositiveSmallIntegerField(
        'Рейтинг',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField('Текст отзыва')
    is_published = models.BooleanField('Опубликован', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.customer_name or 'Аноним'} — {self.rating} ★"
