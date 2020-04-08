# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .country import PyCountry
from .father import PyFather

POSITION_CHOICE = (
    ("before", "Antes de la Cantidad"),
    ('after', 'Después de la Cantidad'),
)


class PyCurrency(PyFather):
    name = models.CharField('Nombre', max_length=40)
    alias = models.CharField('Alias', max_length=40)
    symbol = models.CharField('Símbolo', max_length=15)
    country = models.ForeignKey(PyCountry, on_delete=models.PROTECT)
    iso = models.CharField(max_length=30)
    position = models.CharField(
        choices=POSITION_CHOICE, max_length=64, default='after')


    def __str__(self):
        return "{} ({})".format(self.name, self.country)

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
