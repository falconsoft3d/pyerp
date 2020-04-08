# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Localfolder Library
from ..models.employee import PyEmployee

""" BEGIN EMPLEOYEE """
EMPLEOYEE_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Segundo Nombre', 'field': 'name2'},
    {'string': 'Primer Apelllido', 'field': 'first_name'},
    {'string': 'Segundo Apelllido', 'field': 'last_name'},
    {'string': 'Teléfono', 'field': 'phone'},
    {'string': 'Email', 'field': 'email'},
]

EMPLEOYEE_FIELDS_SHORT = ['name', 'name2', 'email', 'first_name', 'last_name', 'phone', 'email']


class EmployeeListView(LoginRequiredMixin, ListView):
    model = PyEmployee
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['title'] = 'Empleados'
        context['detail_url'] = 'payroll:employee-detail'
        context['add_url'] = 'payroll:employee-add'
        context['fields'] = EMPLEOYEE_FIELDS
        return context


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = PyEmployee
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'payroll:employee', 'name': 'Empleados'}]
        context['update_url'] = 'payroll:employee-update'
        context['delete_url'] = 'payroll:employee-delete'
        context['fields'] = EMPLEOYEE_FIELDS
        return context


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = PyEmployee
    fields = EMPLEOYEE_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Empleado'
        context['breadcrumbs'] = [{'url': 'payroll:employee', 'name': 'Empleado'}]
        context['back_url'] = reverse('payroll:employee')
        return context


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = PyEmployee
    fields = EMPLEOYEE_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'payroll:employee', 'name': 'Empleados'}]
        context['back_url'] = reverse('payroll:employee-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteEmployee(self, pk):
    employee = PyEmployee.objects.get(id=pk)
    employee.delete()
    return redirect(reverse('payroll:employee'))
