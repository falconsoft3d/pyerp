# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather

CRON_CHOICE = (
    ("minutes", "Minutes"),
    ('hours', 'Hours'),
    ('day', 'Day'),
    ('work_day', 'Work Day'),
    ('weeks', 'Weeks'),
    ('month', 'Month'),
)


class PyCron(PyFather):
    name = models.CharField('Nombre', max_length=40)
    active = models.BooleanField('Activo', default=False)
    interval_type = models.CharField(
        choices=CRON_CHOICE, max_length=64, default='hours')
    model_name = models.CharField('Modelo', max_length=40)
    function = models.CharField('Método', max_length=40)
    number_call = models.IntegerField('Número de llamadas', default=-1)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)


    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Cron")
        verbose_name_plural = _("Crons")
