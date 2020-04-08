# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyMenu
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Parent"), 'field': 'parent_id'},
    {'string': _("Link"), 'field': 'link'},
    {'string': _("Sequence"), 'field': 'sequence'},
]

OBJECT_FORM_FIELDS = ['name', 'parent_id', 'link', 'sequence']


class MenuListView(LoginRequiredMixin, FatherListView):
    model = PyMenu
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class MenuDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyMenu
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class MenuCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyMenu
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class MenuUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyMenu
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class MenuDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyMenu
    success_url = 'base:menus'
