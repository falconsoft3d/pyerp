# Django Library
from django.urls import path

# Localfolder Library
from ..views.menu import (
    MenuCreateView, MenuDeleteView, MenuDetailView, MenuListView,
    MenuUpdateView)

app_name = 'PyMenu'

urlpatterns = [
    path('', MenuListView.as_view(), name='list'),
    path('add/', MenuCreateView.as_view(), name='add'),
    path('<int:pk>/', MenuDetailView.as_view(), name='detail'),
    path('<int:pk>/update', MenuUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', MenuDeleteView.as_view(), name='delete'),
]
