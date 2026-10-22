from django.db import models


class CalculatorCategory(models.Model):
    """Категории работ (чистка, замена, диагностика...)"""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField(unique=True)
    base_price = models.DecimalField('Базовая цена', max_digits=8, decimal_places=2)
    is_active = models.BooleanField('Активна', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'

    def __str__(self):
        return self.name


class CalculatorOption(models.Model):
    """Дополнительные опции (срочность, выезд и т.д.)"""
    category = models.ForeignKey(
        CalculatorCategory,
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='Категория'
    )
    name = models.CharField('Название опции', max_length=200)
    extra_price = models.DecimalField('Доп. цена', max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Опция'
        verbose_name_plural = 'Опции'

    def __str__(self):
        return f"{self.category} - {self.name}"
