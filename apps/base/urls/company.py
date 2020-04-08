"""uRLs para company
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.company import (
    CompanyAutoComplete, CompanyCreateView, CompanyDeleteView,
    CompanyDetailView, CompanyListView, CompanyUpdateView,
    change_active_company)

app_name = 'PyCompany'

urlpatterns = [
    path('', CompanyListView.as_view(), name='list'),
    path('add/', CompanyCreateView.as_view(), name='add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='delete'),
    path('<int:company>/change/', change_active_company, name='change'),
    # ===================== Auto completado de Company ===================== #
    path('autocomplete', CompanyAutoComplete.as_view(), name='autocomplete'),
]
