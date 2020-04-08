# Standard Library
import os

# Django Library
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..rename_image import RenameImage
from .country import PyCountry
from .father import PyFather

TYPE_CHOICE = (
    ("company", _("Company")),
    ("individual", _("Individual")),
    ("address", _("Address")),
    ("contact", _("Contact")),
)

_UNSAVED_FILEFIELD = 'unsaved_filefield'


def image_path(instance, filename):
    root, ext = os.path.splitext(filename)
    return "partner/{id}{ext}".format(id=instance.pk, ext=ext)


class PyPartner(PyFather):
    name = models.CharField(_("Name"), max_length=40)
    street = models.CharField(_("Street"), max_length=100, blank=True)
    street_2 = models.CharField(_("Street Other"), max_length=100, blank=True)
    country_id = models.ForeignKey(
        PyCountry,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    city = models.CharField(_("City"), max_length=50, blank=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    email = models.EmailField(_("Email"), max_length=40, blank=True)
    customer = models.BooleanField(_("Customer"), default=True)
    provider = models.BooleanField(_("Provider"), default=True)
    for_invoice = models.BooleanField(_("For Invoice"), default=True)
    note = models.TextField(blank=True, null=True)
    not_email = models.BooleanField(_("No Email"), default=False)
    parent_id = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        default=None,
        on_delete=models.PROTECT,
        verbose_name=_('Partner parent')
    )
    img = models.ImageField(
        max_length=255,
        storage=RenameImage(),
        upload_to=image_path,
        blank=True,
        null=True,
        default='partner/default_partner.png'
    )
    type = models.CharField(
        _("type"),
        choices=TYPE_CHOICE,
        max_length=64,
        default='company'
    )

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, email):
        """Crea un partner de manera sencilla
        """
        pypartner = cls(name=name, email=email)
        pypartner.save()
        return pypartner

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')


@receiver(pre_save, sender=PyPartner)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.img)
        instance.img = 'partner/default_partner.png'


@receiver(post_save, sender=PyPartner)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.img = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
    if not instance.img or instance.img is None:
        instance.img = 'partner/default_partner.png'
        instance.save()
