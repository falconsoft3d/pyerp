# Django Library
from django.urls import path

# Localfolder Library
from ..views.product_brand import (
    ProductBrandCreateView, ProductBrandDeleteView, ProductBrandDetailView,
    ProductBrandListView, ProductBrandUpdateView)

app_name = 'PyProductBrand'

urlpatterns = [
    path('', ProductBrandListView.as_view(), name='list'),
    path('add/', ProductBrandCreateView.as_view(), name='add'),
    path('<int:pk>/', ProductBrandDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ProductBrandUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductBrandDeleteView.as_view(), name='delete'),
]
