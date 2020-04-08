"""uRLs para gestionar las monedas
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.currency import (
    CurrencyAutoComplete, CurrencyCreateView, CurrencyDeleteView,
    CurrencyDetailView, CurrencyListView, CurrencyUpdateView)

app_name = 'PyCurrency'

urlpatterns = [
    path('', CurrencyListView.as_view(), name='list'),
    path('add/', CurrencyCreateView.as_view(), name='add'),
    path('<int:pk>/', CurrencyDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CurrencyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CurrencyDeleteView.as_view(), name='delete'),

    # ====================== Rutas de Auto Completado ====================== #
    path('autocomplete', CurrencyAutoComplete.as_view(), name='autocomplete'),
]
