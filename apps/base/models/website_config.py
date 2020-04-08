# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather


class PyWebsiteConfig(PyFather):
    show_blog = models.BooleanField(_("Show Blog"), default=False)
    show_shop = models.BooleanField(_("Show Shop"), default=False)
    show_price = models.BooleanField(_("Show price"), default=True)
    show_chat = models.BooleanField(_("Show chat"), default=False)
    under_construction = models.BooleanField(_("Under Construction"), default=False)
    user_register = models.BooleanField(_("User Register"), default=False)


    @classmethod
    def create(cls, company):
        wbaseconfig = cls(company_id=company)
        wbaseconfig.save()
        return wbaseconfig

    def get_absolute_url(self):
        return reverse('base:website-config', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("WebsiteConfig")
        verbose_name_plural = _("PyWebsiteConfig")
