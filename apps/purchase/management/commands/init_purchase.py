"""Inicialización de PyERP
"""

# Django Library
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.purchase.models import PyPurchaseOrderState


class Command(BaseCommand):
    """Clase para inicialización de PySaleOrder
    """
    help = (
        _("Command to initialize PyPurchaseOrder")
    )

    def handle(self, *args, **options):

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Generating  purchase migrations...'))
        )
        call_command('makemigrations', 'purchase', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Migrating the purchase database...'))
        )
        call_command('migrate', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp purchase object...')
            )
        )
        if not PyPurchaseOrderState.objects.all().exists():
            call_command('loaddata', 'PyPurchaseOrderState')
