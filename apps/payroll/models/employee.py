# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


# Tabla de Empleados
class PyEmployee(PyFather):
    name = models.CharField('Nombre', max_length=80)
    name2 = models.CharField('Segundo Nombre', max_length=80, blank=True)
    first_name = models.CharField('Apellido Paterno', max_length=80, blank=True)
    last_name = models.CharField('Apellido Materno', max_length=80, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.CharField('Correo', max_length=40, blank=True)

    def get_absolute_url(self):
        return reverse('payroll:employee-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
