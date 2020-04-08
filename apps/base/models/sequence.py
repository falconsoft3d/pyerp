# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .father import PyFather


class PySequence(PyFather):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=100,
        unique=True
    )
    prefix = models.CharField(_("Prefix"), max_length=40, default='default')
    padding = models.PositiveIntegerField(
        verbose_name=_("padding"),
        default=4
    )
    initial = models.PositiveIntegerField(
        verbose_name=_("initial"),
        default=1
    )
    increment = models.PositiveIntegerField(
        verbose_name=_("increment"),
        default=1
    )
    reset = models.PositiveIntegerField(
        verbose_name=_("reset"),
        null=True,
        blank=True
    )
    last = models.PositiveIntegerField(verbose_name=_("Last"), editable=False)
    next_val = models.PositiveIntegerField(verbose_name=_("Next"))

    class Meta:
        verbose_name = _("sequence")
        verbose_name_plural = _("sequences")

    def __str__(self):
        return "name={}, prefix={}, last={}".format(
            repr(self.name), repr(self.prefix), repr(self.last))
