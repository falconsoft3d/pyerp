# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyChannel(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    code = models.CharField(_("Code"), null=True, blank=True, max_length=6)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("PyChannel")
