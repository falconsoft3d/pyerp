# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyEmail
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Title"), 'field': 'title'},
    {'string': _("Creation Date"), 'field': 'fc'},
    {'string': _("Partner"), 'field': 'partner_id'},
    {'string': _("Type"), 'field': 'type'}
]

OBJECT_FORM_FIELDS = ['title', 'content', 'partner_id', 'type']


class EmailListView(LoginRequiredMixin, FatherListView):
    model = PyEmail
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class EmailDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyEmail
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class EmailCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyEmail
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class EmailUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyEmail
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class EmailDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyEmail
