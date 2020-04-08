# Django Library
from django.urls import path

# Localfolder Library
from .views.paypal_config import UpdatePaypalConfigView

# http://www.secnot.com/django-shop-paypal-rest-1.html

app_name = 'paypal'

urlpatterns = [
    path('paypal-config/<int:pk>', UpdatePaypalConfigView.as_view(), name='paypal-config'),
]
