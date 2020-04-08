# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


class PyPage(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    keywords = models.CharField('Keywords', max_length=20, blank=True)


    def __str__(self):
        return format(self.title)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("PyPage")
