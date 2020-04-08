# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyCountry(PyFather):
    name = models.CharField(_("Name"), max_length=60)

    def __str__(self):
        return format(self.name)


    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("PyCountry")
