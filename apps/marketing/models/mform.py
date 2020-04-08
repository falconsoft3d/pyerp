# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather

# Localfolder Library
from .campaign import PyCampaign


class PyMform(PyFather):
    name = models.CharField('Nombre', max_length=255)
    campaign_id = models.ForeignKey(PyCampaign, null=True, blank=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('marketing:mform-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
