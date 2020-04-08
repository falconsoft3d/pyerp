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
from .father import PyFather
from .product_brand import PyProductBrand
from .product_category import PyProductCategory
from .product_webcategory import PyProductWebCategory
from .tax import PyTax
from .uom import PyUom

_UNSAVED_FILEFIELD = 'unsaved_filefield'


def image_path(instance, filename):
    root, ext = os.path.splitext(filename)
    return "product/{id}{ext}".format(id=instance.pk, ext=ext)


PRODUCT_CHOICE = (
    ("product", "Almacenable"),
    ('consu', 'Consumible'),
    ('service', 'Servicio'),
    ('software', 'Software')
)


class PyProduct(PyFather):
    name = models.CharField(_("Name"), max_length=80)
    code = models.CharField(_("Code"), max_length=80, blank=True)
    bar_code = models.CharField(_("Bar Code"), max_length=80, blank=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, default=1)
    cost = models.DecimalField(_("Cost"), max_digits=10, decimal_places=2, default=0)
    category_id = models.ForeignKey(
        PyProductCategory,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Category')
    )
    web_category_id = models.ForeignKey(
        PyProductWebCategory,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Web category')
    )
    description = models.TextField(_("Description"), blank=True, null=True)
    features = models.TextField(_("Features"), blank=True, null=True)
    uom_id = models.ForeignKey(PyUom, null=True, blank=True, on_delete=models.PROTECT)
    brand_id = models.ForeignKey(
        PyProductBrand,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Brand')
    )
    tax = models.ManyToManyField(PyTax, blank=True)
    youtube_video = models.CharField(null=True, blank=True, max_length=300)
    img = models.ImageField(
        max_length=255,
        storage=RenameImage(),
        upload_to=image_path,
        blank=True,
        null=True,
        default='product/default_product.png'
    )

    web_active = models.BooleanField('Web', default=False)
    pos_active = models.BooleanField('POS', default=False)
    share = models.BooleanField(_("Share"), default=False)
    featured = models.BooleanField(_("Featured"), default=False)

    type = models.CharField(_("type"), choices=PRODUCT_CHOICE, max_length=64, default='consu')


    def __str__(self):
        return format(self.name)

    @classmethod
    def suma(cls):
        return cls.__name__

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")



@receiver(pre_save, sender=PyProduct)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.img)
        instance.img = 'product/default_product.png'


@receiver(post_save, sender=PyProduct)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.img = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
    if not instance.img or instance.img is None:
        instance.img = 'product/default_product.png'
        instance.save()
