# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

# Localfolder Library
from ..models import PyCron
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Activo', 'field': 'active'},
    {'string': 'Ejecutar Cada', 'field': 'interval_type'},
    {'string': 'Modelo', 'field': 'model_name'},
    {'string': 'Método', 'field': 'function'},
    {'string': 'Número de Llamadas', 'field': 'number_call'},
    {'string': 'Creado en', 'field': 'created_on'},
]

OBJECT_FORM_FIELDS = ['name', 'active', 'interval_type', 'model_name', 'function', 'number_call']


class CronListView(LoginRequiredMixin, FatherListView):
    model = PyCron
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class CronDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyCron
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class CronCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyCron
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CronUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyCron
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CronDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyCron
