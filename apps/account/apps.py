# Django Library
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountConfig(AppConfig):
    name = 'apps.account'
    verbose_name = _('accounts')

    def ready(self):
        import apps.account.signals  # noqa
