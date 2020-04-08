"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.post import (
    PostCreateView, PostDeleteView, PostDetailView, PostListView,
    PostUpdateView)

app_name = 'PyPost'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
