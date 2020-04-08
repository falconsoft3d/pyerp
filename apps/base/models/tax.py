# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyTax(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2, default=0)
    include_price = models.BooleanField(_("Include Price"), default=True, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tax")
        verbose_name_plural = _("PyTax")
