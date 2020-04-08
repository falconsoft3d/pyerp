# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.father import PyFather

TYPE = (
        ("indicator", "Indicator"),
        ("table", "Table"),
    )

class PyBi(PyFather):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=255)
    type = models.CharField(_("Type"), null=True, blank=True,  choices=TYPE, max_length=64, default='indicator')
    model = models.CharField(_("Model"), null=True, blank=True,  max_length=50)
    parameter = models.CharField(_("Parameter"), null=True, blank=True, max_length=50)
    color = models.CharField(_("Color"), null=True, blank=True, max_length=50, default="indianred")
    font_color = models.CharField(_("Font Color"), null=True, blank=True, max_length=50, default="white")
    icon = models.CharField(_("Icon"), null=True, blank=True, max_length=50, default="ion-person-add")
    dashboard = models.CharField(_("Dashboard"), null=True, blank=True, max_length=50, default="home")
    url = models.CharField(_("URL"), null=True, blank=True, max_length=50, default="PyPartner:list")


    def __str__(self):
        return format(self.name)

    class Meta:
        verbose_name = _("Bi")
        verbose_name_plural = _("Bi")
