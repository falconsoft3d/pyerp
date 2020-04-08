"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.event import (
    EventCreateView, EventDeleteView, EventDetailView, EventListView,
    EventUpdateView)

app_name = 'PyEvent'

urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('add/', EventCreateView.as_view(), name='add'),
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
    path('<int:pk>/update', EventUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='delete'),
]
