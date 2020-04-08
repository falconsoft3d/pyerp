# Django Library
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PurchaseConfig(AppConfig):
    name = 'apps.purchase'
    verbose_name = _('purchases')

    def ready(self):
        import apps.purchase.signals  # noqa
