# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


class PyMeta(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()


    def __str__(self):
        return format(self.title)

    class Meta:
        verbose_name = _("Meta")
        verbose_name_plural = _("PyMeta")
