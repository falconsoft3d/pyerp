"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.note import (
    NoteCreateView, NoteDeleteView, NoteDetailView, NoteListView,
    NoteUpdateView)

app_name = 'PyNote'

urlpatterns = [
    path('', NoteListView.as_view(), name='list'),
    path('add/', NoteCreateView.as_view(), name='add'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('<int:pk>/update', NoteUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='delete'),
]
