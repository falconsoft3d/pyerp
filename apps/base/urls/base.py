"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views import Install, ProviderListView, UpdateBaseConfigView
from ..views.base_config import LoadData
from ..views.home import erp_home
from ..views.web_father import active_object, inactive_object
from ..views.website_config import UpdateWebsiteConfigView

app_name = 'base'

urlpatterns = [
    path('', erp_home, name='home'),
    path('install', Install, name='install'),
    path('config/<int:pk>', UpdateBaseConfigView.as_view(), name='base-config'),
    path('load-data', LoadData, name='load-data'),

    path(
        'website-config/<int:pk>',
        UpdateWebsiteConfigView.as_view(),
        name='website-config'
    ),

    path('provider', ProviderListView.as_view(), name='provider'),

    path('active_object', active_object, name='active-object'),
    path('inactive_object', inactive_object, name='inactive-object'),
]
