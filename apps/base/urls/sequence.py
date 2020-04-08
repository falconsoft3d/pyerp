"""uRLs para tax
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.sequence import (
    SequenceCreateView, SequenceDeleteView, SequenceDetailView,
    SequenceListView, SequenceUpdateView)

app_name = 'PySequence'

urlpatterns = [
    path('', SequenceListView.as_view(), name='list'),
    path('add/', SequenceCreateView.as_view(), name='add'),
    path('<int:pk>/', SequenceDetailView.as_view(), name='detail'),
    path('<int:pk>/update', SequenceUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SequenceDeleteView.as_view(), name='delete'),
]
