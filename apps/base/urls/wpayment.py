"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.wpayment import (
    WPaymentCreateView, WPaymentDeleteView, WPaymentDetailView,
    WPaymentListView, WPaymentUpdateView)

app_name = 'PyWPayment'

urlpatterns = [
    path('', WPaymentListView.as_view(), name='list'),
    path('add/', WPaymentCreateView.as_view(), name='add'),
    path('<int:pk>/', WPaymentDetailView.as_view(), name='detail'),
    path('<int:pk>/update', WPaymentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', WPaymentDeleteView.as_view(), name='delete'),
]
