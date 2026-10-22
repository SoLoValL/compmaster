from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteSettings(models.Model):
    """Глобальные настройки сайта (телефон, адрес, email, соцсети, SEO)."""
    phone = models.CharField(_("Телефон"), max_length=20, blank=True)
    address = models.TextField(_("Адрес"), blank=True)
    email = models.EmailField(_("Email"), blank=True)
    seo_title = models.CharField(_("SEO заголовок"), max_length=150, blank=True)
    seo_description = models.TextField(_("SEO описание"), blank=True)

    class Meta:
        verbose_name = _("Настройки сайта")
        verbose_name_plural = _("Настройки сайта")

    def __str__(self):
        return "Настройки сайта"


class SliderItem(models.Model):
    """Слайдер на главной странице (заголовок, текст, картинка)."""
    title = models.CharField(_("Заголовок слайда"), max_length=100)
    text = models.TextField(_("Текст слайда"), blank=True)
    image = models.ImageField(_("Изображение"), upload_to="sliders/", blank=True, null=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активен"), default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Слайд")
        verbose_name_plural = _("Слайды")

    def __str__(self):
        return self.title
