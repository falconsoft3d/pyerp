"""Rutas de PyErp
"""
# Django Library
# Librerias Django
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.static import serve

# Thirdparty Library
# Librerias de terceros
from apps.base.views import ActivateLanguageView
from pyerp.settings import BASE_DIR

urlpatterns = [
    path('', include('apps.base.home_urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
    # path('', include('apps.home.urls')),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        '<language_code>/language/activate/',
        ActivateLanguageView.as_view(),
        name='activate_language'
    ),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]


# ========================================================================== #
# Recorrer el archivo de aplicaciones instaladas y construir sus rutas
with open('%s/installed_apps.py' % BASE_DIR, 'r') as ins_apps_file:
    for line in ins_apps_file.readlines():
        if line.strip() == 'apps.home':
            urlpatterns.pop(0)
            urlpatterns += [path('', include('apps.home.urls'))]

        elif line.strip() == 'apps.webodoobim':
            urlpatterns.pop(0)
            urlpatterns += [path('', include('apps.webodoobim.urls'))]

        else:
            _, app = line.split('.')
            urlpatterns += [
                path(
                    '{}/'.format(app.rstrip('\n')),
                    include('{}.urls'.format(line.strip()))
                )
            ]
