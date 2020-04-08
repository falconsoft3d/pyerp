"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.shop import WebProductDetailView, WebProductListView

app_name = 'PyShop'

urlpatterns = [
    path('', WebProductListView.as_view(), name='shop'),
    path('product/<int:pk>/', WebProductDetailView.as_view(), name='product'),
]
