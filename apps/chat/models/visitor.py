# Standard Library
import datetime

# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


# Tabla de Departamentos
class PyVisitor(PyFather):
    name = models.CharField('Nombre', max_length=80, null=True, blank=True)
    sid = models.CharField('SID', max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base:visitor-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)


class PyChatHistory(PyFather):

    visitor = models.ForeignKey(PyVisitor, models.CASCADE, 'Visitante')
    message = models.CharField('Mensaje', max_length=500)
    response = models.BooleanField('Respuesta', default=False)
    datetime = models.DateTimeField('Fecha y hora', null=True, blank=True)
