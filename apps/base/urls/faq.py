"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.faq import (
    FaqCreateView, FaqDeleteView, FaqDetailView, FaqListView, FaqUpdateView)

app_name = 'PyFaq'

urlpatterns = [
    path('', FaqListView.as_view(), name='list'),
    path('add/', FaqCreateView.as_view(), name='add'),
    path('<int:pk>/', FaqDetailView.as_view(), name='detail'),
    path('<int:pk>/update', FaqUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', FaqDeleteView.as_view(), name='delete'),
]
