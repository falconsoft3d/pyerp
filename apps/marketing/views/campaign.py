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
from ..models import PyCampaign

CAMPAIGN_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Código', 'field': 'code'},
        ]

CAMPAIGN_FIELDS_SHORT = ['name','code']


class CampaignListView(LoginRequiredMixin, ListView):
    model = PyCampaign
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CampaignListView, self).get_context_data(**kwargs)
        context['title'] = 'Campañas'
        context['detail_url'] = 'marketing:campaign-detail'
        context['add_url'] = 'marketing:campaign-add'
        context['fields'] = CAMPAIGN_FIELDS
        return context

class CampaignDetailView(LoginRequiredMixin, DetailView):
    model = PyCampaign
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'marketing:campaign', 'name': 'Campaña'}]
        context['update_url'] = 'marketing:campaign-update'
        context['delete_url'] = 'marketing:campaign-delete'
        context['fields'] = CAMPAIGN_FIELDS
        return context

class CampaignCreateView(LoginRequiredMixin, CreateView):
    model = PyCampaign
    fields = CAMPAIGN_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CampaignCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Campaña'
        context['breadcrumbs'] = [{'url': 'marketing:campaign', 'name': 'Campaña'}]
        context['back_url'] = reverse('marketing:campaign')
        return context

class CampaignUpdateView(LoginRequiredMixin, UpdateView):
    model = PyCampaign
    fields = CAMPAIGN_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CampaignUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'marketing:campaign', 'name': 'Campaña'}]
        context['back_url'] = reverse('marketing:campaign-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteCampaign(self, pk):
    campaign = PyCampaign.objects.get(id=pk)
    campaign.delete()
    return redirect(reverse('marketing:campaign'))
