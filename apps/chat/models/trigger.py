# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


class PyTrigger(PyFather):
    question = models.CharField(_("Question"), max_length=300, blank=True, null=True)
    answer = models.TextField(_("Answer"), blank=True, null=True)
    init = models.BooleanField(_("Init"),default=False)

    def get_absolute_url(self):
        return reverse('base:trigger-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.question)
