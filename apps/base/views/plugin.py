# Standard Library
import json
import subprocess
import sys
from collections import OrderedDict
from importlib import reload
from os import listdir, path

# Django Library
from django.apps import apps
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import clear_url_caches, reverse

# Localfolder Library
from ...base.models import PyPlugin
from .web_father import FatherListView

OBJECT_LIST_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Author', 'field': 'author'},
    {'string': 'Description', 'field': 'description'},
    {'string': 'Installed', 'field': 'installed'},
]

def Apps(request):
    return render(request, 'base/plugin.html')


class PluginListView(LoginRequiredMixin, FatherListView):
    model = PyPlugin
    template_name = 'base/plugin.html'
    fields = OBJECT_LIST_FIELDS
    context_object_name = 'plugin_list'
    paginate_by = 12


# ========================================================================== #
def PluginUpdate(self):
    """Actualiza los plugins
    """
    FILE_NAME = 'info.json'
    folder_apps = '{}/apps'.format(settings.BASE_DIR)
    plugin_list = tuple(
        set(name['name'] for name in PyPlugin.objects.all().values('name'))
    )
    for folder in listdir(folder_apps):
        file = folder_apps + "/" + folder + "/" + FILE_NAME
        if path.isfile(file) and folder not in plugin_list:
            print(file)
            with open(file) as json_file:
                data = json.load(json_file)
                plugin = PyPlugin(
                    name=data['name'].lower(),
                    description=data['description'],
                    author=data['author'],
                    fa=data['fa'],
                    version=data['version'],
                    website=data['website'],
                    color=data['color']
                )
                plugin.save()

    return redirect(reverse('PyPlugin:list'))



def PluginInstall(self, pk):
    plugin = PyPlugin.objects.get(id=pk)
    plugin.installed = True
    with open('installed_apps.py', 'a+') as installed_apps_file:
        if installed_apps_file.write('apps.{}\n'.format(plugin.name.lower())):
            print('yes')
        else:
            print("no")

    # Como no se cargar una sola app, se leen todas las app que estan
    # como plugins en tiempo de ejecución al instalar cualquier app
    with open('%s/installed_apps.py' % settings.BASE_DIR, 'r') as ins_apps_file:
        for line in ins_apps_file.readlines():
            settings.INSTALLED_APPS += (line.strip().rstrip('\n'), )

    apps.app_configs = OrderedDict()
    apps.apps_ready = apps.models_ready = apps.loading = apps.ready = False
    apps.clear_cache()

    try:
        # Se recargan todas las aplicaciones ¿como cargar solo una?
        apps.populate(settings.INSTALLED_APPS)
    except:
        # plugin.installed = False
        print('Fallo el proceso de poblado de la app')

    try:
        # Se contruyen las migraciones del plugin
        call_command('makemigrations', plugin.name.lower(), interactive=False)
    except:
        # plugin.installed = False
        print('No hay migración de la app')

    try:
        # Se ejecutan las migraciones de la app
        call_command('migrate', plugin.name.lower(), interactive=False)
    except:
        # plugin.installed = False
        print('No se migro la app')

    try:
        # Se ejecutan las migraciones de la app
        call_command('loaddata', '{}.json'.format(plugin.name.lower()), interactive=False)
    except:
        # plugin.installed = False
        print('No se cargaron datos de la app')

    plugin.save()

    # subprocess.run[PROJECT_RELOAD]
    # Recargo en memoria la rutas del proyecto
    urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        clear_url_caches()
        reload(sys.modules[urlconf])

    return redirect(reverse('PyPlugin:list'))


# ========================================================================== #
def PluginUninstall(self, pk):
    app = PyPlugin.objects.get(id=pk)
    app.installed = False
    app.save()
    app_lists = []
    with open('installed_apps.py', 'r') as installed_apps_file:
        app_lists = installed_apps_file.readlines()
    with open('installed_apps.py', 'w+') as installed_apps_file:
        for line in app_lists:
            if 'apps.%s' % app.name.lower() == line.strip():
                continue
            installed_apps_file.write(line)
    return redirect(reverse('PyPlugin:list'))
