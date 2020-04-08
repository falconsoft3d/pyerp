# Django Library
from django.urls import path

# Localfolder Library
from ..views.variant import (
    VariantCreateView, VariantDeleteView, VariantDetailView, VariantListView,
    VariantUpdateView)

app_name = 'PyVariant'

urlpatterns = [
    path('list', VariantListView.as_view(), name='list'),
    path('add/', VariantCreateView.as_view(), name='add'),
    path('<int:pk>/', VariantDetailView.as_view(), name='detail'),
    path('<int:pk>/update', VariantUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', VariantDeleteView.as_view(), name='delete'),
]
