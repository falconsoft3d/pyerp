"""Inicialización de PyERP
"""

# Django Library
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.sale.models import PySaleOrderState


class Command(BaseCommand):
    """Clase para inicialización de PySaleOrder
    """
    help = (
        _("Command to initialize PySaleOrder")
    )

    def handle(self, *args, **options):

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Generating  sale migrations...'))
        )
        call_command('makemigrations', 'sale', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Migrating the sale database...'))
        )
        call_command('migrate', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp sale object...')
            )
        )
        if not PySaleOrderState.objects.all().exists():
            call_command('loaddata', 'PySaleOrderState')
