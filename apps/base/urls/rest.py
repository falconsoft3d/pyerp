# Django Library
from django.contrib import admin
from django.urls import path

# Localfolder Library
from ..views.rest import loginApiRest

urlpatterns = [
    path('login', loginApiRest)
]
