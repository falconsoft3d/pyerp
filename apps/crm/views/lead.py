# Django Library
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Localfolder Library
from ..models.lead import PyLead

""" BEGIN LEAD """
LEAD_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Cliente', 'field': 'partner_id'},
            {'string': 'Vendedor', 'field': 'user_id'},
            {'string': 'Ingreso', 'field': 'income'},
            {'string': 'Etapa', 'field': 'stage_id'},
            {'string': 'Contenido', 'field': 'content'},
        ]

LEAD_FIELDS_VIEW = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Cliente', 'field': 'partner_id'},
            {'string': 'Vendedor', 'field': 'user_id'},
            {'string': 'Ingreso', 'field': 'income'},
            {'string': 'Etapa', 'field': 'stage_id'},
            {'string': 'Contenido', 'field': 'content'},
        ]

LEAD_FIELDS_SHORT = ['name','partner_id','user_id','income','stage_id','content']


class LeadListView(LoginRequiredMixin, ListView):
    model = PyLead
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['title'] = 'Oportunidades'
        context['detail_url'] = 'crm:lead-detail'
        context['add_url'] = 'crm:lead-add'
        context['fields'] = LEAD_FIELDS_VIEW
        return context

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = PyLead
    template_name = 'base/detail.html'
    login_url = "login"
    def get_context_data(self, **kwargs):
        context = super(LeadDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'crm:lead', 'name': 'Oportunidad'}]
        context['update_url'] = 'crm:lead-update'
        context['delete_url'] = 'crm:lead-delete'
        context['fields'] = LEAD_FIELDS_VIEW
        return context

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = PyLead
    fields = LEAD_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(LeadCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Lead'
        context['breadcrumbs'] = [{'url': 'crm:lead', 'name': 'Oportunidad'}]
        context['back_url'] = reverse('crm:lead')
        return context

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = PyLead
    fields = LEAD_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'crm:lead', 'name': 'Oportunidad'}]
        context['back_url'] = reverse('crm:lead-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteLead(self, pk):
    lead = PyLead.objects.get(id=pk)
    lead.delete()
    return redirect(reverse('crm:lead'))
