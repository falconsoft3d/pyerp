# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyNote
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("Color"), 'field': 'color'},
]

OBJECT_FORM_FIELDS = ['name', 'note', 'color']


class NoteListView(LoginRequiredMixin, FatherListView):
    model = PyNote
    template_name = 'base/note_list.html'


class NoteDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyNote
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class NoteCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyNote
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class NoteUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyNote
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class NoteDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyNote
