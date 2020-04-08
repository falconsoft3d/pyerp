"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.message import (
    MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView,
    MessageUpdateView)

app_name = 'PyMessage'

urlpatterns = [
    path('', MessageListView.as_view(), name='list'),
    path('add/', MessageCreateView.as_view(), name='add'),
    path('<int:pk>/', MessageDetailView.as_view(), name='detail'),
    path('<int:pk>/update', MessageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', MessageDeleteView.as_view(), name='delete'),
]
