"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.meta import (
    MetaCreateView, MetaDeleteView, MetaDetailView, MetaListView,
    MetaUpdateView)

app_name = 'PyMeta'

urlpatterns = [
    path('', MetaListView.as_view(), name='list'),
    path('add/', MetaCreateView.as_view(), name='add'),
    path('<int:pk>/', MetaDetailView.as_view(), name='detail'),
    path('<int:pk>/update', MetaUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', MetaDeleteView.as_view(), name='delete'),
]
