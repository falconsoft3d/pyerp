# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyTag
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

OBJECT_FORM_FIELDS = ['name']


class TagListView(LoginRequiredMixin, FatherListView):
    model = PyTag
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class TagDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyTag
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class TagCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyTag
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class TagUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyTag
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class TagDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyTag
    success_url = 'base:tags'
