"""Rutas del módulo de ordenes de venta
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..reports.invoicepdf import invoice_pdf
from ..views import (
    InvoiceCreateView, InvoiceDeleteView, InvoiceDetailView, InvoiceListView,
    InvoiceUpdateView, invoice_state, load_product, load_tax)

app_name = 'PyInvoice'

urlpatterns = [
    # =========================== Invoice URL's ============================ #
    path('<int:type>/', InvoiceListView.as_view(), name='list'),
    path('<int:pk>/<int:type>/', InvoiceDetailView.as_view(), name='detail'),
    path('add/<int:type>/', InvoiceCreateView.as_view(), name='add'),
    path(
        '<int:pk>/edit/<int:type>/',
        InvoiceUpdateView.as_view(),
        name='update'
    ),
    path(
        '<int:pk>/delete/<int:type>/',
        InvoiceDeleteView.as_view(),
        name='delete'
    ),
    path(
        'state/<int:pk>/<int:state>/<int:type>/',
        invoice_state,
        name='state'
    ),

    # ======================== Invoice= AJAX URL's ========================= #
    path('load-product/', load_product, name='ajax_load_product'),
    path('load-tax/', load_tax, name='ajax_load_tax'),

    # ====================== Invoice= Reports URL's ======================== #
    path('pdf/<int:pk>', invoice_pdf, name='pdf'),
]
