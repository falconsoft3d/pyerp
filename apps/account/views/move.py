"""Sub Vistas del módulo
"""
# Standard Library
import logging

# Django Library
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView

# Thirdparty Library
from apps.base.views.web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

# Localfolder Library
from ..forms import ACCOUNTING_NOTES, AccountMoveForm
from ..models import PyAccountMove, PyAccountMoveDetail

LOGGER = logging.getLogger(__name__)

OBJECT_LIST_FIELDS = [
    {'string': ('Date'), 'field': 'date_move'},
    {'string': _('Name'), 'field': 'name'},
    {'string': ('Company'), 'field': 'company_move'},
    {'string': ('Reference'), 'field': 'reference'},
    {'string': ('Journal'), 'field': 'journal_id'},
    {'string': ('Amount'), 'field': 'credit'},
    {'string': ('State'), 'field': 'state'},
]

OBJECT_DETAIL_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': ('Journal'), 'field': 'journal_id'},
    {'string': ('Date'), 'field': 'date_move'},
    {'string': ('Company'), 'field': 'company_move'},
    {'string': ('Reference'), 'field': 'reference'},
]

DETAIL_OBJECT_LIST_FIELDS = [
    {'string': _('Account'), 'field': 'account_plan_id'},
    {'string': _('Company'), 'field': 'reference_company'},
    {'string': _('Tag'), 'field': 'tags'},
    {'string': ('Debit'), 'field': 'debit'},
    {'string': ('Credit'), 'field': 'credit'},
    {'string': _('Due Date'), 'field': 'date_due'},
]


# ========================================================================== #
class AccountMoveListView(LoginRequiredMixin, FatherListView):
    """Lista de asientos contables
    """
    model = PyAccountMove
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class AccountMoveDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyAccountMove
    template_name = 'move/detail.html'
    extra_context = {
        'master_fields': OBJECT_DETAIL_FIELDS,
        'detail_fields': DETAIL_OBJECT_LIST_FIELDS,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['breadcrumbs'] = [
            {
                'url': '{}:list'.format(object_name),
                'name': '{}'.format(verbose_name)
            },
            {
                'url': False,
                'name': self.object.name
            }
        ]
        # context['print_url'] = '{}:pdf'.format(object_name)
        context['detail'] = PyAccountMoveDetail.objects.filter(
            active=True,
            company_id=self.request.user.active_company_id,
            account_move_id=self.object.pk
        )
        return context


# ========================================================================== #
class AccountMoveCreateView(LoginRequiredMixin, FatherCreateView):
    """Vista para agregar las sale
    """
    model = PyAccountMove
    form_class = AccountMoveForm
    template_name = 'move/form.html'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = 'PyAccountMove:sale-order-add'
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['breadcrumbs'] = [
            {
                'url': '{}:list'.format(object_name),
                'name': '{}'.format(verbose_name)
            }
        ]
        if self.request.POST:
            context['formset'] = ACCOUNTING_NOTES(self.request.POST)
        else:
            context['formset'] = ACCOUNTING_NOTES()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        t_debit = 0
        t_credit = 0
        with transaction.atomic():
            form.instance.uc = self.request.user.pk
            if form.is_valid() and formset.is_valid():
                for obj in formset:
                    print(obj.cleaned_data)
                    if 'DELETE' in obj.cleaned_data.keys() and obj.cleaned_data['DELETE'] is False:
                        t_debit += obj.cleaned_data['debit']
                        t_credit += obj.cleaned_data['credit']
                if t_debit != t_credit:
                    messages.error(
                        self.request,
                        _('Unbalanced accounting entry')
                    )
                    return super().form_invalid(form)

                self.object = form.save()
                formset.instance = self.object
                formset.save()
                return super().form_valid(form)
            else:
                return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('PyAccountMove:detail', kwargs={'pk': self.object.pk})


# ========================================================================== #
class AccountMoveUpdateView(LoginRequiredMixin, FatherUpdateView):
    """Vista para editarar las sale
    """
    model = PyAccountMove
    form_class = AccountMoveForm
    template_name = 'move/form.html'

    def get_context_data(self, **kwargs):
        _pk = self.kwargs.get(self.pk_url_kwarg)
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['breadcrumbs'] = [
            {
                'url': '{}:list'.format(object_name),
                'name': '{}'.format(verbose_name)
            },
            {
                'url': False,
                'name': self.object.name
            }
        ]
        if self.request.POST:
            context['form'] = AccountMoveForm(self.request.POST, instance=self.object)
            context['formset'] = ACCOUNTING_NOTES(self.request.POST, instance=self.object)
        else:
            context['form'] = AccountMoveForm(instance=self.object)
            context['formset'] = ACCOUNTING_NOTES(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        t_debit = 0
        t_credit = 0
        if self.object.state == 0:
            with transaction.atomic():
                form.instance.um = self.request.user.pk
                if form.is_valid() and formset.is_valid():
                    for obj in formset:
                        print(obj.cleaned_data)
                        if 'DELETE' in obj.cleaned_data.keys() and obj.cleaned_data['DELETE'] is False:
                            t_debit += obj.cleaned_data['debit']
                            t_credit += obj.cleaned_data['credit']
                    if t_debit != t_credit:
                        messages.error(
                            self.request,
                            _('Unbalanced accounting entry')
                        )
                        return super().form_invalid(form)

                    self.object = form.save(commit=False)
                    formset.instance = self.object
                    formset.save()
                    self.object.save()
                    return super().form_valid(form)
                else:
                    return super().form_invalid(form)
        else:
            messages.warning(
                self.request,
                _('The current move %(order)s status does not allow updates.') % {'order': self.object.name}
            )
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('PyAccountMove:detail', kwargs={'pk': self.object.pk})


# ========================================================================== #
class AccountMoveDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar las sale
    """
    model = PyAccountMove
    template_name = 'account/delete.html'
    success_url = reverse_lazy('PyAccountMove:list')

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete Invoice')
        context['action_url'] = 'PyAccountMove:delete'
        context['delete_message'] = '<p>¿Está seguro de eliminar la orden de compras <strong>' + self.object.name + '</strong>?</p>'
        context['cant_delete_message'] = '<p>La orden de compras <strong>' + self.object.name + '</strong>, no puede ser eliminada.</p>'
        # context['detail'] = PyAccountMoveDetail.objects.filter(invoice_id=pk).exists()
        context['detail'] = True
        return context

    def delete(self, request, *args, **kwargs):
        # pk = self.kwargs.get(self.pk_url_kwarg)
        # self.object = self.get_object()
        # success_url = self.get_success_url()
        # detail = PyAccountMoveDetail.objects.filter(invoice_id=pk).exists()
        # if not detail:
        #     self.object.delete()
        return HttpResponseRedirect(self.success_url)


# ========================================================================== #
@login_required()
def move_state(request, pk, state):
    invoice = PyAccountMove.objects.get(pk=pk)
    invoice.state = state
    invoice.save()
    return redirect(
        reverse_lazy('PyAccountMove:detail', kwargs={'pk': pk})
    )
