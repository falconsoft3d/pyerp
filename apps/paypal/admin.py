# Django Library
from django.contrib import admin

# Localfolder Library
from .models.paypal_config import PaypalConfig

admin.site.register(PaypalConfig)
