# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Localfolder Library
from ..models.bim_budget import PyBimBudget

BUDGET_BIM_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

BUDGET_BIM_FIELDS_SHORT = ['name']


class BimBudgetListView(LoginRequiredMixin, ListView):
    model = PyBimBudget
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimBudgetListView, self).get_context_data(**kwargs)
        context['title'] = 'Budget'
        context['detail_url'] = 'bim:budget-detail'
        context['add_url'] = 'bim:budget-add'
        context['fields'] = BUDGET_BIM_FIELDS
        return context


class BimBudgetDetailView(LoginRequiredMixin, DetailView):
    model = PyBimBudget
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimBudgetDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'bim:budget', 'name': 'Budget'}]
        context['update_url'] = 'bim:budget-update'
        context['delete_url'] = 'bim:budget-delete'
        context['fields'] = BUDGET_BIM_FIELDS
        return context


class BimBudgetCreateView(LoginRequiredMixin, CreateView):
    model = PyBimBudget
    fields = BUDGET_BIM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimBudgetCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Budget'
        context['breadcrumbs'] = [{'url': 'bim:budget', 'name': 'Budget'}]
        context['back_url'] = reverse('bim:budget')
        return context


class BimBudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = PyBimBudget
    fields = BUDGET_BIM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimBudgetUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'bim:budget', 'name': 'Budget'}]
        context['back_url'] = reverse('bim:budget-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteBimBudget(self, pk):
    budget = PyBimBudget.objects.get(id=pk)
    budget.delete()
    return redirect(reverse('bim:budget'))
