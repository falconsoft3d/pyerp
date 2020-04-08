# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from .company import PyCompany

SHARE_PRODUCT_CHOICE = (
    ("no", "No Share"),
    ("yes_some", "Yes Some"),
    ('yes_all', 'Yes All')
)


class BaseConfig(models.Model):
    online = models.BooleanField('Online', default=False)
    main_company_id = models.ForeignKey(PyCompany, on_delete='cascade', null=True, blank=True)
    open_menu = models.BooleanField('Menu Abierto', default=True)
    load_data = models.BooleanField('Data Cargada', default=False)
    type_share = models.CharField(_("Type Share"), choices=SHARE_PRODUCT_CHOICE, max_length=64, default='no')


    def dload_data(self):
        self.load_data = True

    def get_absolute_url(self):
        return reverse('base:base-config', kwargs={'pk': self.pk})

    @classmethod
    def create(cls, company):
        """Crea un propietario de manera sencilla
        """
        baseconfig = cls(main_company_id=company)
        baseconfig.save()

        return baseconfig
