# Django Library
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SaleConfig(AppConfig):
    name = 'apps.sale'
    verbose_name = _('sales')

    def ready(self):
        import apps.sale.signals  # noqa
