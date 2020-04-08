"""uRLs para tax
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.tax import (
    TaxAutoComplete, TaxCreateView, TaxDeleteView, TaxDetailView, TaxListView,
    TaxUpdateView)

app_name = 'PyTax'

urlpatterns = [
    path('', TaxListView.as_view(), name='list'),
    path('add/', TaxCreateView.as_view(), name='add'),
    path('<int:pk>/', TaxDetailView.as_view(), name='detail'),
    path('<int:pk>/update', TaxUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TaxDeleteView.as_view(), name='delete'),

    # ====================== Rutas de Auto Completado ====================== #
    path('autocomplete', TaxAutoComplete.as_view(), name='autocomplete'),
]
