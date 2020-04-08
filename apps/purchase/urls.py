"""Rutas del módulo de ordenes de venta
"""
# Django Library
from django.urls import path

# Localfolder Library
from .reports.purchaseorderpdf import purchase_order_pdf
from .views import (
    PyPurchaseOrderAddView, PyPurchaseOrderDeleteView,
    PyPurchaseOrderDetailView, PyPurchaseOrderEditView,
    PyPurchaseOrderListView, load_product, load_tax, purchase_order_state)

app_name = 'PyPurchaseOrder'

urlpatterns = [
    # ======================== Purchase Orders URL's ======================= #
    path('purchase-order', PyPurchaseOrderListView.as_view(), name='list'),
    path(
        'purchase-order/<int:pk>',
        PyPurchaseOrderDetailView.as_view(),
        name='detail'
    ),
    path('purchase-order/add/', PyPurchaseOrderAddView.as_view(), name='add'),
    path(
        'purchase-order/<int:pk>/edit/',
        PyPurchaseOrderEditView.as_view(),
        name='update'
    ),
    path(
        'purchase-order/<int:pk>/delete/',
        PyPurchaseOrderDeleteView.as_view(),
        name='delete'
    ),
    path(
        'purchase-order-state/<int:pk>/<int:state>',
        purchase_order_state,
        name='state'
    ),

    # ===================== Purchase Orders AJAX URL's ===================== #
    path(
        'purchase-order/load-product/',
        load_product,
        name='ajax_load_product'
    ),
    path('purchase-order/load-tax/', load_tax, name='ajax_load_tax'),

    # =================== Purchase Orders Reports URL's ==================== #
    path(
        'pdf/<int:pk>',
        purchase_order_pdf,
        name='pdf'
    ),
]
