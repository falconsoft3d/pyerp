"""Rutas del módulo de ordenes de venta
"""
# Django Library
from django.urls import path

# Localfolder Library
from .reports.saleorderpdf import sale_order_pdf
from .views import (
    SaleOrderAddView, SaleOrderDeleteView, SaleOrderDetailView,
    SaleOrderEditView, SaleOrderListView, load_product, load_tax,
    sale_order_state)

app_name = 'PySaleOrder'

urlpatterns = [
    # ========================== Sale Orders URL's ========================= #
    path('sale-order', SaleOrderListView.as_view(), name='list'),
    path('sale-order/<int:pk>', SaleOrderDetailView.as_view(), name='detail'),
    path('sale-order/add/', SaleOrderAddView.as_view(), name='add'),
    path(
        'sale-order/<int:pk>/edit/',
        SaleOrderEditView.as_view(),
        name='update'
    ),
    path(
        'sale-order/<int:pk>/delete/',
        SaleOrderDeleteView.as_view(),
        name='delete'
    ),
    path(
        'sale-order-state/<int:pk>/<int:state>',
        sale_order_state,
        name='state'
    ),

    # ======================== Sale Orders AJAX URL's ====================== #
    path('sale-order/load-product/', load_product, name='ajax_load_product'),
    path('sale-order/load-tax/', load_tax, name='ajax_load_tax'),

    # ====================== Sale Orders Reports URL's ===================== #
    path(
        'pdf/<int:pk>',
        sale_order_pdf,
        name='pdf'
    ),
]
