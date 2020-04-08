# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import PyCountry
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

OBJECT_FORM_FIELDS = ['name']


class CountryListView(LoginRequiredMixin, FatherListView):
    model = PyCountry
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class CountryDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyCountry
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class CountryCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyCountry
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CountryUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyCountry
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CountryDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyCountry


class CountryAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyCountry
    """
    def get_queryset(self):
        queryset = PyCountry.objects.filter(active=True)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
