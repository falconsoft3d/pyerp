"""uRLs para partner
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views import CustomerListView
from ..views.partner import (
    PartnerAutoComplete, PartnerCreateView, PartnerDeleteView,
    PartnerDetailView, PartnerUpdateView)

app_name = 'PyPartner'

urlpatterns = [

    path('', CustomerListView.as_view(), name='list'),
    path('add/', PartnerCreateView.as_view(), name='add'),
    path('<int:pk>/', PartnerDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PartnerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PartnerDeleteView.as_view(), name='delete'),

    # ====================== Rutas de Auto Completado ====================== #
    path('autocomplete', PartnerAutoComplete.as_view(), name='autocomplete'),
]
