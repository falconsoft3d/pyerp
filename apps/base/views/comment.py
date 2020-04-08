# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyComment
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Comment"), 'field': 'comment'},
]

OBJECT_FORM_FIELDS = ['name', 'comment']


class CommentListView(LoginRequiredMixin, FatherListView):
    model = PyComment
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class CommentDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyComment
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class CommentCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyComment
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CommentUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyComment
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CommentDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyComment
