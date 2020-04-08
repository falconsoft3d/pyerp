# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Localfolder Library
from ..models.task import PyTask

TASK_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Proyecto', 'field': 'project_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

TASK_FIELDS_SHORT = ['name','state','project_id','note']


class TaskListView(LoginRequiredMixin, ListView):
    model = PyTask
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['title'] = 'Tareas'
        context['detail_url'] = 'project:task-detail'
        context['add_url'] = 'project:task-add'
        context['fields'] = TASK_FIELDS
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = PyTask
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'project:task', 'name': 'Tarea'}]
        context['update_url'] = 'project:task-update'
        context['delete_url'] = 'project:task-delete'
        context['fields'] = TASK_FIELDS
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = PyTask
    fields = TASK_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        context['breadcrumbs'] = [{'url': 'project:task', 'name': 'Tarea'}]
        context['back_url'] = reverse('project:task')
        return context

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = PyTask
    fields = TASK_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'project:task', 'name': 'Tarea'}]
        context['back_url'] = reverse('project:task-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteTask(self, pk):
    task = PyTask.objects.get(id=pk)
    task.delete()
    return redirect(reverse('project:task'))
