"""Sub Vistas del módulo
"""
# Standard Library
import logging

# Django Library
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView

# Thirdparty Library
from apps.base.models import PyProduct, PyTax
from apps.base.views.web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

# Localfolder Library
from ..forms import PRODUCT_FORMSET, InvoiceForm
from ..models import PyInvoice, PyInvoiceDetail, PyInvoiceState

LOGGER = logging.getLogger(__name__)

OBJECT_LIST_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': _('Client'), 'field': 'partner_id'},
    {'string': ('Date'), 'field': 'date_invoice'},
    {'string': ('State'), 'field': 'state'},
    {'string': ('Net Amount'), 'field': 'amount_untaxed', 'align': 'text-right', 'humanize': True},
    {'string': ('Total'), 'field': 'amount_total', 'align': 'text-right', 'humanize': True},
]

OBJECT_TOTAL_FIELDS = [
    {'string': _('Net Amount or Affection:'), 'field': 'amount_untaxed'},
    {'string': _('Exempt Amount:'), 'field': 'amount_exempt'},
    {'string': _('IVA:'), 'field': 'amount_tax_iva'},
    {'string': _('Other taxes:'), 'field': 'amount_tax_other'},
    {'string': _('Total taxes:'), 'field': 'amount_tax_total'},
    {'string': _('Total:'), 'field': 'amount_total'},
]

OBJECT_DETAIL_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': ('Date'), 'field': 'date_invoice'},
    {'string': _('Client'), 'field': 'partner_id'},
    {'string': _('Seller'), 'field': 'seller_id'},
    {'string': _('Origin'), 'field': 'origin'},
]

DETAIL_OBJECT_LIST_FIELDS = [
    {'string': _('Product'), 'field': 'product_id'},
    {'string': _('Description'), 'field': 'description'},
    {'string': _('Quantity'), 'field': 'quantity', 'align': 'text-center', 'humanize': True},
    {'string': ('UOM'), 'field': 'uom_id', 'align': 'text-left', 'humanize': True},
    {'string': ('Price'), 'field': 'price', 'align': 'text-right', 'humanize': True},
    {'string': _('Discount'), 'field': 'discount', 'align': 'text-right', 'humanize': True},
    {'string': _('Tax'), 'field': 'tax_id'},
    {'string': _('Sub Total'), 'field': 'amount_total', 'align': 'text-right', 'humanize': True},
]


# ========================================================================== #
class InvoiceListView(LoginRequiredMixin, FatherListView):
    """Lista de las ordenes de venta
    """
    model = PyInvoice
    extra_context = {'fields': OBJECT_LIST_FIELDS}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _type = self.kwargs['type']
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['add_url'] = reverse_lazy(
            '{}:add'.format(object_name),
            kwargs={'type': _type}
        )
        context['type'] = _type
        if _type == 1:
            context['breadcrumbs'] = [{
                'url': False,
                'name': _('Customer Invoice')
            }]
        elif _type == 2:
            context['breadcrumbs'] = [{
                'url': False,
                'name': _('Provider Invoice')
            }]
        return context

    def get_queryset(self):
        _type = self.kwargs['type']
        if self.model._meta.object_name in self.EXLUDE_FROM_FILTER:
            queryset = self.model.objects.filter(active=True)
        else:
            queryset = self.model.objects.filter(
                company_id=self.request.user.active_company_id,
                active=True,
                type=_type
            )
        return queryset


# ========================================================================== #
class InvoiceDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyInvoice
    template_name = 'invoice/detail.html'
    extra_context = {
        'master_fields': OBJECT_DETAIL_FIELDS,
        'detail_fields': DETAIL_OBJECT_LIST_FIELDS,
        'total_fields': OBJECT_TOTAL_FIELDS
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _type = self.kwargs['type']
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['back_url'] = reverse_lazy(
            '{}:list'.format(object_name),
            kwargs={'type': _type}
        )
        context['update_url'] = reverse_lazy(
            '{}:update'.format(object_name),
            kwargs={'pk': self.object.pk, 'type': _type}
        )
        context['delete_url'] = reverse_lazy(
            '{}:delete'.format(object_name),
            kwargs={'pk': self.object.pk, 'type': _type}
        )
        forward = self.model.objects.filter(
            pk__gt=self.kwargs['pk'],
            active=True,
            company_id=self.request.user.active_company_id
        ).first()
        backward = self.model.objects.filter(
            pk__lt=self.kwargs['pk'],
            active=True,
            company_id=self.request.user.active_company_id
        ).order_by('-pk').first()
        if forward:
            context['forward'] = reverse_lazy(
                '{}:detail'.format(object_name),
                kwargs={'pk': forward.pk, 'type': _type}
            )
        if backward:
            context['backward'] = reverse_lazy(
                '{}:detail'.format(object_name),
                kwargs={'pk': backward.pk, 'type': _type}
            )

        if _type == 1:
            url_name = _('Customer Invoice')
        elif _type == 2:
            url_name = _('Provider Invoice')

        context['breadcrumbs'] = [
            {
                'url': reverse_lazy(
                    '{}:list'.format(object_name),
                    kwargs={'type': _type}
                ),
                'name': url_name
            },
            {
                'url': False,
                'name': self.object.name
            }
        ]
        context['header_state_botons'] = []
        context['header_state'] = self.object.state.state
        if self.object.state.pk == 1:
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 3, 'type': _type}
                    ),
                    'name': _('Confirm'),
                    'class': 'important'
                }
            )
        if self.object.state.pk not in (2, 4):
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 2, 'type': _type}
                    ),
                    'name': _('Cancel'),
                    'class': ''
                }
            )
        if self.object.state.pk in (2, 3):
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 1, 'type': _type}
                    ),
                    'name': _('Draft'),
                    'class': ''
                }
            )
            # if self.object.state.pk == 3:
            #     context['header_state_botons'].append(
            #         {
            #             'url': reverse_lazy(
            #                 '{}:state'.format(object_name),
            #                 kwargs={'pk': self.object.pk, 'state': 4}
            #             ),
            #             'name': _('To Invoice'),
            #             'class': ''
            #         }
            #     )
        context['print_url'] = '{}:pdf'.format(object_name)
        context['detail'] = PyInvoiceDetail.objects.filter(
            active=True,
            company_id=self.request.user.active_company_id,
            invoice_id=self.object.pk
        )
        return context


# ========================================================================== #
class InvoiceCreateView(LoginRequiredMixin, FatherCreateView):
    """Vista para agregar las sale
    """
    model = PyInvoice
    form_class = InvoiceForm
    template_name = 'invoice/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _type = self.kwargs['type']
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        data = {'type': _type}
        context['form'] = InvoiceForm(initial=data)

        if _type == 1:
            url_name = _('Customer Invoice')
        elif _type == 2:
            url_name = _('Provider Invoice')

        context['breadcrumbs'] = [
            {
                'url': reverse_lazy(
                    '{}:list'.format(object_name),
                    kwargs={'type': _type}
                ),
                'name': url_name
            }
        ]
        context['back_url'] = reverse_lazy(
            '{}:list'.format(object_name),
            kwargs={'type': _type}
        )
        context['type'] = _type
        if self.request.POST:
            context['formset'] = PRODUCT_FORMSET(self.request.POST)
        else:
            context['formset'] = PRODUCT_FORMSET()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            form.instance.uc = self.request.user.pk
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        _type = self.kwargs['type']
        return reverse_lazy(
            'PyInvoice:detail',
            kwargs={'pk': self.object.pk, 'type': _type}
        )


# ========================================================================== #
class InvoiceUpdateView(LoginRequiredMixin, FatherUpdateView):
    """Vista para editarar las sale
    """
    model = PyInvoice
    form_class = InvoiceForm
    template_name = 'invoice/form.html'

    def get_context_data(self, **kwargs):
        _pk = self.kwargs.get(self.pk_url_kwarg)
        _type = self.kwargs['type']
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['back_url'] = reverse_lazy(
            '{}:detail'.format(object_name),
            kwargs={'pk': self.object.pk, 'type': _type}
        )
        context['delete_url'] = reverse_lazy(
            '{}:delete'.format(object_name),
            kwargs={'pk': self.object.pk, 'type': _type}
        )
        forward = self.model.objects.filter(
            pk__gt=self.kwargs['pk'],
            active=True,
            company_id=self.request.user.active_company_id
        ).first()
        backward = self.model.objects.filter(
            pk__lt=self.kwargs['pk'],
            active=True,
            company_id=self.request.user.active_company_id
        ).order_by('-pk').first()
        if forward:
            context['forward'] = reverse_lazy(
                '{}:detail'.format(object_name),
                kwargs={'pk': forward.pk, 'type': _type}
            )
        if backward:
            context['backward'] = reverse_lazy(
                '{}:detail'.format(object_name),
                kwargs={'pk': backward.pk, 'type': _type}
            )

        if _type == 1:
            url_name = _('Customer Invoice')
        elif _type == 2:
            url_name = _('Provider Invoice')

        context['breadcrumbs'] = [
            {
                'url': reverse_lazy(
                    '{}:list'.format(object_name),
                    kwargs={'type': _type}
                ),
                'name': url_name
            },
            {
                'url': False,
                'name': self.object.name
            }
        ]
        context['header_state_botons'] = []
        context['header_state'] = self.object.state.state
        if self.object.state.pk == 1:
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 3, 'type': _type}
                    ),
                    'name': _('Confirm'),
                    'class': 'important'
                }
            )
        if self.object.state.pk not in (2, 4):
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 2, 'type': _type}
                    ),
                    'name': _('Cancel'),
                    'class': ''
                }
            )
        if self.object.state.pk in (2, 3):
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 1, 'type': _type}
                    ),
                    'name': _('Draft'),
                    'class': ''
                }
            )
            # if self.object.state.pk == 3:
            #     context['header_state_botons'].append(
            #         {
            #             'url': reverse_lazy(
            #                 '{}:state'.format(object_name),
            #                 kwargs={'pk': self.object.pk, 'state': 4}
            #             ),
            #             'name': _('To Invoice'),
            #             'class': ''
            #         }
            #     )
        context['print_url'] = '{}:pdf'.format(object_name)
        if self.request.POST:
            context['form'] = InvoiceForm(self.request.POST, instance=self.object)
            context['formset'] = PRODUCT_FORMSET(self.request.POST, instance=self.object)
        else:
            context['form'] = InvoiceForm(instance=self.object)
            context['formset'] = PRODUCT_FORMSET(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if self.object.state.pk == 1:
            with transaction.atomic():
                form.instance.um = self.request.user.pk
                if form.is_valid() and formset.is_valid():
                    print("Form valid")
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
                _('The current invoice %(obj)s status does not allow updates.') % {'obj': self.object.name}
            )
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        _type = self.kwargs['type']
        return reverse_lazy(
            'PyInvoice:detail',
            kwargs={'pk': self.object.pk, 'type': _type}
        )


# ========================================================================== #
class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar las sale
    """
    model = PyInvoice
    template_name = 'account/delete.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete Invoice')
        context['action_url'] = 'PyInvoice:delete'
        context['delete_message'] = '<p>¿Está seguro de eliminar la orden de compras <strong>' + self.object.name + '</strong>?</p>'
        context['cant_delete_message'] = '<p>La orden de compras <strong>' + self.object.name + '</strong>, no puede ser eliminada.</p>'
        # context['detail'] = PyInvoiceDetail.objects.filter(invoice_id=pk).exists()
        context['detail'] = True
        return context

    def delete(self, request, *args, **kwargs):
        # pk = self.kwargs.get(self.pk_url_kwarg)
        # self.object = self.get_object()
        # success_url = self.get_success_url()
        # detail = PyInvoiceDetail.objects.filter(invoice_id=pk).exists()
        # if not detail:
        #     self.object.delete()
        return HttpResponseRedirect(self.success_url)


# ========================================================================== #
@login_required()
def load_product(request):
    context = {}
    product_id = request.GET.get('product')
    product = PyProduct.objects.filter(pk=product_id)
    context['product'] = serializers.serialize('json', product)
    return JsonResponse(data=context, safe=False)


# ========================================================================== #
@login_required()
def load_tax(request):
    context = {}
    tax_id = request.GET.getlist('tax[]')
    tax = PyTax.objects.filter(pk__in=tax_id)
    context['tax'] = serializers.serialize('json', tax)
    return JsonResponse(data=context, safe=False)


# ========================================================================== #
@login_required()
def invoice_state(request, pk, state, type):
    invoice = PyInvoice.objects.get(pk=pk)
    state = PyInvoiceState.objects.get(pk=state)
    if invoice.state != 4:
        with transaction.atomic():
            invoice.state = state
            invoice.save()
            # if state == 4:
            #     invoice = sale_order_to_invoice(request, sale_order)
            #     return redirect(
            #         reverse_lazy('PyInvoice:detail', kwargs={'pk': invoice.pk})
            #     )
    else:
        messages.warning(
                self.request,
                _('The current invoice %(invoice)s status does not allow updates.') % {'invoice': self.object.name}
            )
    return redirect(
        reverse_lazy('PyInvoice:detail', kwargs={'pk': pk, 'type': type})
    )
