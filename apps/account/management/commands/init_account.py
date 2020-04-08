"""Inicialización de PyERP
"""

# Django Library
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.account.models import PyInvoiceState


class Command(BaseCommand):
    """Clase para inicialización de PySaleOrder
    """
    help = (
        _("Command to initialize PySaleOrder")
    )

    def handle(self, *args, **options):

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Generating  account migrations...'))
        )
        call_command('makemigrations', 'account', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Migrating the account database...'))
        )
        call_command('migrate', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp invoice object...')
            )
        )
        if not PyInvoiceState.objects.all().exists():
            call_command('loaddata', 'PyInvoiceState')
