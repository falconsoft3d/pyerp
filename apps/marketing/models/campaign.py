# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


class PyCampaign(PyFather):
    name = models.CharField('Nombre', max_length=80)
    code = models.CharField('Código', max_length=13)

    def get_absolute_url(self):
        return reverse('marketing:campaign-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
