# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.views.web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)
from dal import autocomplete

# Localfolder Library
from ..models import PyJournal

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Short Code"), 'field': 'short_code'},
    {'string': _("Defaul Credit Account"), 'field': 'default_credit_account'},
    {'string': _("Default Debit Account"), 'field': 'default_debit_account'},
    {'string': _("Type"), 'field': 'type'},
]

OBJECT_FORM_FIELDS = [
    'name',
    'short_code',
    'default_credit_account',
    'default_debit_account',
    'type',
]


class JournalListView(LoginRequiredMixin, FatherListView):
    model = PyJournal
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class JournalDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyJournal
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class JournalCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyJournal
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class JournalUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyJournal
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class JournalDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyJournal


# ========================================================================== #
class JournalAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        queryset = PyJournal.objects.filter(active=True)

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
