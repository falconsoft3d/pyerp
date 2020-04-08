"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.email import (
    EmailCreateView, EmailDeleteView, EmailDetailView, EmailListView,
    EmailUpdateView)

app_name = 'PyEmail'

urlpatterns = [
    path('', EmailListView.as_view(), name='list'),
    path('add/', EmailCreateView.as_view(), name='add'),
    path('<int:pk>/', EmailDetailView.as_view(), name='detail'),
    path('<int:pk>/update', EmailUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', EmailDeleteView.as_view(), name='delete'),
]
