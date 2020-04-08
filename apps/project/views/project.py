# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Localfolder Library
from ..models.project import PyProject

PROJECT_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Notas', 'field': 'note'},
        ]

PROJECT_FIELDS_SHORT = ['name','state', 'note']


class ProjectListView(LoginRequiredMixin, ListView):
    model = PyProject
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Proyectos'
        context['detail_url'] = 'project:project-detail'
        context['add_url'] = 'project:project-add'
        context['fields'] = PROJECT_FIELDS
        return context

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = PyProject
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'project:project', 'name': 'Proyecto'}]
        context['update_url'] = 'project:project-update'
        context['delete_url'] = 'project:project-delete'
        context['fields'] = PROJECT_FIELDS
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = PyProject
    fields = PROJECT_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Proyecto'
        context['breadcrumbs'] = [{'url': 'project:project', 'name': 'Proyecto'}]
        context['back_url'] = reverse('project:project')
        return context

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = PyProject
    fields = PROJECT_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'project:project', 'name': 'Proyecto'}]
        context['back_url'] = reverse('project:project-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteProject(self, pk):
    project = PyProject.objects.get(id=pk)
    project.delete()
    return redirect(reverse('project:project'))
