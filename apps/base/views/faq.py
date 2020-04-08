# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyFaq
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Content"), 'field': 'content'},
]

OBJECT_FORM_FIELDS = ['name', 'content']


class FaqListView(LoginRequiredMixin, FatherListView):
    model = PyFaq
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class FaqDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyFaq
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class FaqCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyFaq
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class FaqUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyFaq
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class FaqDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyFaq
