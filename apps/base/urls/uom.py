"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.uom import (
    UomAutoComplete, UomCreateView, UomDeleteView, UomDetailView, UomListView,
    UomUpdateView)

app_name = 'PyUom'

urlpatterns = [
    path('', UomListView.as_view(), name='list'),
    path('add/', UomCreateView.as_view(), name='add'),
    path('<int:pk>/', UomDetailView.as_view(), name='detail'),
    path('<int:pk>/update', UomUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UomDeleteView.as_view(), name='delete'),
    # ==================== Auto completado de Productos ==================== #
    path('autocomplete', UomAutoComplete.as_view(), name='autocomplete'),
]
