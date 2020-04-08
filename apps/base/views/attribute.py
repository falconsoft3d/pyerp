# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyAttribute
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Variant"), 'field': 'variant_id'},
]

OBJECT_FORM_FIELDS = ['name','variant_id']


class AttributeListView(LoginRequiredMixin, FatherListView):
    model = PyAttribute
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class AttributeDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyAttribute
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class AttributeCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyAttribute
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class AttributeUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyAttribute
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class AttributeDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyAttribute
