
# Standard Library
import os

# Django Library
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..rename_image import RenameImage
from .country import PyCountry
from .currency import PyCurrency
from .father import PyFather

_UNSAVED_FILEFIELD = 'unsaved_filefield'


def image_path(instance, filename):
    root, ext = os.path.splitext(filename)
    return "logo/{id}{ext}".format(id=instance.pk, ext=ext)


class PyCompany(PyFather):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100, blank=True)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=40, blank=True)

    country = models.ForeignKey(PyCountry, on_delete=models.PROTECT)
    currency_id = models.ForeignKey(PyCurrency, null=True, blank=True, on_delete=models.PROTECT)

    postal_code = models.CharField(max_length=255, blank=True)

    social_facebook = models.CharField(max_length=255, blank=True)
    social_instagram = models.CharField(max_length=255, blank=True)
    social_linkedin = models.CharField(max_length=255, blank=True)
    social_youtube = models.CharField(max_length=255, blank=True)
    social_whatsapp = models.CharField(max_length=255, blank=True)

    def giveme_main_color():
        count = PyCompany.objects.all().count()
        if count == 0:
            return "#563D7C"
        elif count == 1:
            return "#026AA7"
        elif count == 2:
            return "#01363D"
        else:
            return "#fff"

    def giveme_content_wrapper_color():
        count = PyCompany.objects.all().count()
        if count == 0:
            return "#f4f6f9"
        elif count == 1:
            return "#f4f6f9"
        elif count == 2:
            return "#f4f6f9"
        else:
            return "#f4f6f9"

    def giveme_font_color():
        count = PyCompany.objects.all().count()
        if count == 0:
            return "#cbbde2"
        elif count == 1:
            return "#CCE1ED"
        elif count == 2:
            return "#30AABC"
        else:
            return "#777"

    main_color = models.CharField(max_length=20, blank=True, default=giveme_main_color)
    content_wrapper_color = models.CharField(max_length=20, blank=True, default=giveme_content_wrapper_color)
    font_color = models.CharField(max_length=20, blank=True, default=giveme_font_color)

    slogan = models.CharField('Eslogan', max_length=250, blank=True)
    logo = models.ImageField(
        max_length=255,
        storage=RenameImage(),
        upload_to=image_path,
        blank=True,
        null=True,
        default='logo/default_logo.png'
    )

    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.name)

    @classmethod
    def create(cls, name, country, currency, company_id):
        """Crea un propietario de manera sencilla
        """
        if company_id:
            pycompany = cls(name=name, country=country, currency_id=currency, company_id=company_id)
        else:
            pycompany = cls(name=name, country=country, currency_id=currency)

        pycompany.save()

        return pycompany

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("PyCompany")


@receiver(pre_save, sender=PyCompany)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.logo)
        instance.logo = 'logo/default_logo.png'


@receiver(post_save, sender=PyCompany)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.logo = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
    if not instance.logo or instance.logo is None:
        instance.logo = 'logo/default_logo.png'
        instance.save()
