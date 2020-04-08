# Django Library
from django.apps import apps
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import clear_url_caches, reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Thirdparty Library
from pyerp.settings import BASE_DIR

# Localfolder Library
from ..forms import AvatarForm
from ..models import (
    BaseConfig, PyCompany, PyLog, PyPartner, PyPlugin, PyProduct,
    PyProductCategory, PyUser, PyWebsiteConfig)
from .activatelanguage import ActivateLanguageView
from .base_config import UpdateBaseConfigView
from .company import (
    CompanyCreateView, CompanyDeleteView, CompanyDetailView, CompanyListView,
    CompanyUpdateView, change_active_company, CompanyAutoComplete)
from .partner import CustomerListView, ProviderListView
from .usercustom import (
    ActivateUserView, AvatarUpdateView, LogOutModalView, PasswordRecoveryView,
    ProfileView, SignUpView, cambio_clave)
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)
from .wparameter import PyWParameter
from .uom import (
    UomCreateView, UomDeleteView, UomDetailView, UomListView, UomUpdateView, UomAutoComplete)


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

def Install(request):
    return render(request, 'base/install.html')

OBJECT_LIST_FIELDS = [
    {'string': _('Name'), 'field': 'first_name'},
    {'string': _('Last name'), 'field': 'last_name'},
    {'string': _('Email'), 'field': 'email'},
]

OBJECT_FORM_FIELDS = ['email', 'first_name', 'last_name']


class UserListView(LoginRequiredMixin, FatherListView):
    model = PyUser
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class UserDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyUser
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].email
        context['breadcrumbs'] = [{'url': 'PyUser:list', 'name': 'Usuarios'}]
        context['update_url'] = 'PyUser:update'
        context['delete_url'] = 'PyUser:delete'
        context['buttons'] = [
            {
                'act': reverse('PyUser:password-change', kwargs={'pk': context['object'].pk}),
                'name': 'Cambiar contraseña',
                'class': 'success'
            }
        ]
        return context


class UserCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyUser
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'
    success_url = 'PyUser:detail'

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        company = self.request.user.active_company
        self.object = PyUser.create(first_name, last_name, email, password, 0, 0, 1, company)
        url = reverse_lazy(self.get_success_url(), kwargs={'pk': self.object.pk})

        return HttpResponseRedirect(url)


class UserUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyUser
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        company = self.request.user.active_company
        self.object = PyUser.create(first_name, last_name, email, password, 0, 0, 1, company)
        url = reverse_lazy(self.get_success_url(), kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyUser


@login_required()
def ChangePasswordForm(self, pk):
    return render(self, 'base/change_password.html', {'pk': pk})


@login_required()
def DoChangePassword(self, pk, **kwargs):
    user = PyUser.objects.get(id=pk)
    if user and self.POST['new_password1'] == self.POST['new_password2']:
        user.set_password(self.POST['new_password1'])
    else:
        return render(self, 'base/change_password.html', {'pk': pk, 'error': 'Passwords do not match.'})
    return redirect(reverse('PyUser:user-detail', kwargs={'pk': pk}))
