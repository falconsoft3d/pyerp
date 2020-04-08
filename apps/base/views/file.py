# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyFile
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("User"), 'field': 'user_id'},
]

OBJECT_FORM_FIELDS = ['name', 'note', 'user_id']


class FileListView(LoginRequiredMixin, FatherListView):
    model = PyFile
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class FileDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyFile
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class FileCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyFile
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class FileUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyFile
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class FileDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyFile
    success_url = 'base:files'
