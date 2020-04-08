# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyPlugin(PyFather):
    name = models.CharField(_("Name"), max_length=80)
    author = models.CharField(_("Author"), max_length=80)
    description = models.TextField(_("description"), blank=True, null=True)
    installed = models.BooleanField(default=False, blank=True, null=True)
    website = models.CharField(_("Website"), blank=True, null=True, max_length=180)
    color = models.CharField(_("Color"), blank=True, null=True, max_length=20)
    fa = models.CharField(_("Icon"), blank=True, null=True, max_length=20)
    version = models.CharField(_("Version"), blank=True, null=True, max_length=20)
    sequence = models.IntegerField(_("Sequence"), default=100)


    def __str__(self):
        return format(self.name)

    class Meta:
        ordering = ['pk']
        verbose_name = _("Plugin")
        verbose_name_plural = _("PyPlugin")
