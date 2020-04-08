# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyVariant
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

OBJECT_FORM_FIELDS = ['name']


class VariantListView(LoginRequiredMixin, FatherListView):
    model = PyVariant
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class VariantDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyVariant
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class VariantCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyVariant
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class VariantUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyVariant
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class VariantDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyVariant
    success_url = 'base:variants'
