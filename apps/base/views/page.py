# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.page import PyPage
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
            {'string': _("Title"), 'field': 'title'},
            {'string': _("Created on"), 'field': 'created_on'},
            {'string': _("Keywords"), 'field': 'keywords'},

        ]

OBJECT_FORM_FIELDS = ['title', 'content', 'keywords']


class PageListView(LoginRequiredMixin, FatherListView):
    model = PyPage
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class PageDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPage
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class PageCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyPage
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class PageUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyPage
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class PageDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyPage
