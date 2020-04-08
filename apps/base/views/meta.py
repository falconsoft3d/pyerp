# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.meta import PyMeta
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Title"), 'field': 'title'},
    {'string': _("Content"), 'field': 'content'},
]

OBJECT_FORM_FIELDS = ['title', 'content']


class MetaListView(LoginRequiredMixin, FatherListView):
    model = PyMeta
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class MetaDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyMeta
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class MetaCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyMeta
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class MetaUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyMeta
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class MetaDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyMeta
