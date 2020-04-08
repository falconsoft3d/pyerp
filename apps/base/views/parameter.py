# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyParameter
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Value"), 'field': 'value'},
]

OBJECT_FORM_FIELDS = ['name', 'value']


class ParameterListView(LoginRequiredMixin, FatherListView):
    model = PyParameter
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ParameterDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyParameter
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ParameterCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyParameter
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ParameterUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyParameter
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ParameterDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyParameter
