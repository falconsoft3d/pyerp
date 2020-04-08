# Django Library
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather

ALPHANUMERIC = RegexValidator(
    r'^[0-9a-z_]*$',
    _('Only lowercase alphanumeric characters and underscore are allowed.')
)


class PyWParameter(PyFather):
    name = models.CharField(
        _('Name'),
        max_length=100,
        validators=[ALPHANUMERIC],
        unique=True
        )
    value = models.CharField(_('Value'), max_length=255)



    class Meta:
        ordering = ['-id']
        verbose_name = _("WParameter")
        verbose_name_plural = _("PyWParameters")

    def __str__(self):
        return format(self.name)
