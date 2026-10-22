from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Расширенная модель пользователя (можно добавить мастеров и клиентов)."""
    is_master = models.BooleanField(_("Мастер"), default=False)
    phone = models.CharField(_("Телефон"), max_length=20, blank=True)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")


class MasterProfile(models.Model):
    """Профиль мастера: навыки, опыт, фото, описание."""
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="master_profile")
    photo = models.ImageField(_("Фото мастера"), upload_to="masters/", blank=True, null=True)
    bio = models.TextField(_("О себе / опыт"), blank=True)
    skills = models.TextField(_("Навыки (через запятую)"), blank=True, help_text=_("Например: Windows, macOS, чистка ноутбуков, замена SSD"))
    rating = models.DecimalField(_("Рейтинг"), max_digits=3, decimal_places=2, default=0.00)
    is_available = models.BooleanField(_("Доступен для заказов"), default=True)

    class Meta:
        verbose_name = _("Профиль мастера")
        verbose_name_plural = _("Профили мастеров")

    def __str__(self):
        return f"{self.user.get_full_name()} (мастер)"
