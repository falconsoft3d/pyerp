"""uRLs para gestionar los paises
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.country import (
    CountryAutoComplete, CountryCreateView, CountryDeleteView,
    CountryDetailView, CountryListView, CountryUpdateView)

app_name = 'PyCountry'

urlpatterns = [
    path('', CountryListView.as_view(), name='list'),
    path('add/', CountryCreateView.as_view(), name='add'),
    path('<int:pk>/', CountryDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CountryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CountryDeleteView.as_view(), name='delete'),

    # ====================== Rutas de Auto Completado ====================== #
    path('autocomplete', CountryAutoComplete.as_view(), name='autocomplete'),
]
