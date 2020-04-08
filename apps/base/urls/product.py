# Django Library
from django.urls import path

# Localfolder Library
from ..views.product import (
    ProductAutoComplete, ProductCreateView, ProductDeleteView,
    ProductDetailView, ProductListView, ProductUpdateView)

app_name = 'PyProduct'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('add/', ProductCreateView.as_view(), name='add'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    # ==================== Auto completado de Productos ==================== #
    path('autocomplete', ProductAutoComplete.as_view(), name='autocomplete'),
]
