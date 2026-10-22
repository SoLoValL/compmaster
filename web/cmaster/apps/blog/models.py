from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Post(models.Model):
    """Статья блога."""
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField('Краткое описание', blank=True,
                               help_text='Краткое описание для списка статей')
    content = models.TextField('Содержание')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='blog_posts', verbose_name='Автор'
    )
    image = models.ImageField('Обложка', upload_to='blog/', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
