# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyImage
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Content"), 'field': 'content'},
]

OBJECT_FORM_FIELDS = ['name', 'content']


class ImageListView(LoginRequiredMixin, FatherListView):
    model = PyImage
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ImageDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyImage
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ImageCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyImage
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ImageUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyImage
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ImageDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyImage
