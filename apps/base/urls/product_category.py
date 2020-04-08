"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.product_category import (
    ProductCategoryCreateView, ProductCategoryDeleteView,
    ProductCategoryDetailView, ProductCategoryListView,
    ProductCategoryUpdateView)

app_name = 'PyProductCategory'

urlpatterns = [
    path('', ProductCategoryListView.as_view(), name='list'),
    path('add/', ProductCategoryCreateView.as_view(), name='add'),
    path('<int:pk>/', ProductCategoryDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ProductCategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductCategoryDeleteView.as_view(), name='delete'),
]
