"""Inicialización de PyERP
"""

# Standard Library
import json
from os import listdir, path
from time import sleep

# Django Library
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import (
    PyCountry, PyCurrency, PyParameter, PyPlugin, PyWParameter)


class Command(BaseCommand):
    """Clase para inicialización de PyERP
    """
    help = (
        _("Command to install PyErp plugins in testing")
    )

    def handle(self, *args, **options):

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Install plugins in testing...')
            )
        )
        installed_plugin = PyPlugin.objects.filter(installed=True)
        app_counnter = 0
        for plugin in installed_plugin:
            app_counnter += 1
            comand_app = 'init_{}'.format(plugin.name)
            call_command(comand_app,)
        self.stdout.write('Installed {} plugin(s)'.format(app_counnter))
