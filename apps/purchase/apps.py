# Django Library
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PurchaseConfig(AppConfig):
    name = 'apps.purchase'
    verbose_name = _('purchases')
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import apps.purchase.signals  # noqa
