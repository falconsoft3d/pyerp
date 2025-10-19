# Django Library
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountConfig(AppConfig):
    name = 'apps.account'
    verbose_name = _('accounts')
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import apps.account.signals  # noqa
