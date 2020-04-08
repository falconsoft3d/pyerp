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
from ..models import PyMform

MFORM_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Campaña', 'field': 'campaign_id'},
        ]

MFORM_FIELDS_VIEW = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Campaña', 'field': 'campaign_id'},
        ]

MFORM_FIELDS_SHORT = ['name','campaign_id']


class MformListView(LoginRequiredMixin, ListView):
    model = PyMform
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MformListView, self).get_context_data(**kwargs)
        context['title'] = 'Formularios'
        context['detail_url'] = 'marketing:mform-detail'
        context['add_url'] = 'marketing:mform-add'
        context['fields'] = MFORM_FIELDS_VIEW
        return context

class MformDetailView(LoginRequiredMixin, DetailView):
    model = PyMform
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(MformDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'marketing:mform', 'name': 'Formulario'}]
        context['update_url'] = 'marketing:mform-update'
        context['delete_url'] = 'marketing:mform-delete'
        context['fields'] = MFORM_FIELDS_VIEW
        return context

class MformCreateView(LoginRequiredMixin, CreateView):
    model = PyMform
    fields = MFORM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MformCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Formulario'
        context['breadcrumbs'] = [{'url': 'marketing:mform', 'name': 'Formulario'}]
        context['back_url'] = reverse('marketing:mform')
        return context

class MformUpdateView(LoginRequiredMixin, UpdateView):
    model = PyMform
    fields = MFORM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MformUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'marketing:mform', 'name': 'Formulario'}]
        context['back_url'] = reverse('marketing:mform-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteMform(self, pk):
    mform = PyMform.objects.get(id=pk)
    mform.delete()
    return redirect(reverse('marketing:mform'))
