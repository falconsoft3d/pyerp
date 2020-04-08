# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.views.web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)
from dal import autocomplete

# Localfolder Library
from ..models import PyAccountPlan

OBJECT_LIST_FIELDS = [
    {'string': _("Code"), 'field': 'code'},
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Reconcile"), 'field': 'reconcile'},
]

OBJECT_FORM_FIELDS = [
    'code',
    'name',
    'type',
    'tags',
    'reconcile',
    'discontinued',
    'tax_id'
]


class AccountPlanListView(LoginRequiredMixin, FatherListView):
    model = PyAccountPlan
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class AccountPlanDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyAccountPlan
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class AccountPlanCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyAccountPlan
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class AccountPlanUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyAccountPlan
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class AccountPlanDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyAccountPlan


# ========================================================================== #
class AccountPlanAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        queryset = PyAccountPlan.objects.filter(active=True)

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
