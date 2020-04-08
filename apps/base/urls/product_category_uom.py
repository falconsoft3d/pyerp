"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.product_category_uom import (
    ProductCategoryUOMCreateView, ProductCategoryUOMDeleteView,
    ProductCategoryUOMDetailView, ProductCategoryUOMListView,
    ProductCategoryUOMUpdateView)

app_name = 'PyProductCategoryUOM'

urlpatterns = [
    path('', ProductCategoryUOMListView.as_view(), name='list'),
    path('add/', ProductCategoryUOMCreateView.as_view(), name='add'),
    path('int:pk>/', ProductCategoryUOMDetailView.as_view(), name='product-category-uom-detail'),
    path('<int:pk>/update', ProductCategoryUOMUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductCategoryUOMDeleteView.as_view(), name='delete'),
]
