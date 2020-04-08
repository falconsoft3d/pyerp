"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.cron import (
    CronCreateView, CronDeleteView, CronDetailView, CronListView,
    CronUpdateView)

app_name = 'PyCron'

urlpatterns = [
    path('', CronListView.as_view(), name='list'),
    path('add/', CronCreateView.as_view(), name='add'),
    path('<int:pk>/', CronDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CronUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CronDeleteView.as_view(), name='delete'),
]
