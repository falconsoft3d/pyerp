"""uRLs para base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.product_webcategory import (
    ProductWebCategoryCreateView, ProductWebCategoryDeleteView,
    ProductWebCategoryDetailView, ProductWebCategoryListView,
    ProductWebCategoryUpdateView)

app_name = 'PyProductWebCategory'

urlpatterns = [
    path('', ProductWebCategoryListView.as_view(), name='list'),
    path('add/', ProductWebCategoryCreateView.as_view(), name='add'),
    path('<int:pk>/', ProductWebCategoryDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ProductWebCategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductWebCategoryDeleteView.as_view(), name='delete'),
]
