# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Localfolder Library
from ..models.bim_project import PyBimProject

PROJECT_BIM_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

PROJECT_BIM_FIELDS_SHORT = ['name']


class BimProjectListView(LoginRequiredMixin, ListView):
    model = PyBimProject
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Project'
        context['detail_url'] = 'bim:project-detail'
        context['add_url'] = 'bim:project-add'
        context['fields'] = PROJECT_BIM_FIELDS
        return context


class BimProjectDetailView(LoginRequiredMixin, DetailView):
    model = PyBimProject
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimProjectDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'bim:project', 'name': 'Project'}]
        context['update_url'] = 'bim:project-update'
        context['delete_url'] = 'bim:project-delete'
        context['fields'] = PROJECT_BIM_FIELDS
        return context


class BimProjectCreateView(LoginRequiredMixin, CreateView):
    model = PyBimProject
    fields = PROJECT_BIM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimProjectCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Project'
        context['breadcrumbs'] = [{'url': 'bim:project', 'name': 'Project'}]
        context['back_url'] = reverse('bim:project')
        return context


class BimProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = PyBimProject
    fields = PROJECT_BIM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BimProjectUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'bim:project', 'name': 'Project'}]
        context['back_url'] = reverse('bim:project-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteBimProject(self, pk):
    project = PyBimProject.objects.get(id=pk)
    project.delete()
    return redirect(reverse('bim:project'))
