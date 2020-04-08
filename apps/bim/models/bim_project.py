# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


class PyBimProject(PyFather):
    name = models.CharField(_("Name"), max_length=80)

    def get_absolute_url(self):
        return reverse('bim:project-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
