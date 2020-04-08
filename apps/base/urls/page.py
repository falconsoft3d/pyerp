"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.page import (
    PageCreateView, PageDeleteView, PageDetailView, PageListView,
    PageUpdateView)

app_name = 'PyPage'

urlpatterns = [
    path('', PageListView.as_view(), name='list'),
    path('add/', PageCreateView.as_view(), name='add'),
    path('<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='delete'),
]
