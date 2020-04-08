# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import PyProduct, PyUom
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Ratio"), 'field': 'ratio'},
    {'string': _("Rouding"), 'field': 'rouding'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Category"), 'field': 'category_id'},
]

OBJECT_FORM_FIELDS = ['name', 'ratio', 'rouding', 'type', 'category_id']


class UomListView(LoginRequiredMixin, FatherListView):
    model = PyUom
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class UomDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyUom
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class UomCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyUom
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class UomUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyUom
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class UomDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyUom


# ========================================================================== #
class UomAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        queryset = PyUom.objects.filter(active=True)

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
