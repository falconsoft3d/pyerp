# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyProductCategoryUOM(PyFather):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)


    class Meta:
        verbose_name = _("ProductCategory")
        verbose_name_plural = _("PyProductCategory")
