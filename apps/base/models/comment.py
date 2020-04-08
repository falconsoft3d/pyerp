# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyComment(PyFather):
    name = models.CharField('Nombre', max_length=40)
    comment = models.TextField(_("Comment"))
    email = models.EmailField('Correo', max_length=40, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("PyComment")
