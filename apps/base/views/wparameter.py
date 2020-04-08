# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyWParameter
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Value"), 'field': 'value'},
]

OBJECT_FORM_FIELDS = ['name', 'value']


class WParameterListView(LoginRequiredMixin, FatherListView):
    model = PyWParameter
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class WParameterDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyWParameter
    template_name = 'base/detail.html'

class WParameterCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyWParameter
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class WParameterUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyWParameter
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'



class WParameterDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyWParameter
    success_url = 'base:wparameters'
