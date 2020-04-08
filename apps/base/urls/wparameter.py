"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.wparameter import (
    WParameterCreateView, WParameterDeleteView, WParameterDetailView,
    WParameterListView, WParameterUpdateView)

app_name = 'PyWParameter'

urlpatterns = [
    path('', WParameterListView.as_view(), name='list'),
    path('add/', WParameterCreateView.as_view(), name='add'),
    path('<int:pk>/', WParameterDetailView.as_view(), name='detail'),
    path('<int:pk>/update', WParameterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', WParameterDeleteView.as_view(), name='delete'),
]
