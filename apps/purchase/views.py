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
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView

# Thirdparty Library
from apps.account.models import PyInvoice, PyInvoiceDetail
from apps.base.models import PyProduct, PyTax
from apps.base.views.web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

# Localfolder Library
from .forms import PRODUCT_FORMSET, PyPurchaseOrderForm
from .models import (
    PyPurchaseOrder, PyPurchaseOrderDetail, PyPurchaseOrderState)

LOGGER = logging.getLogger(__name__)

OBJECT_LIST_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': _('Client'), 'field': 'partner_id'},
    {'string': ('Date'), 'field': 'date_order'},
    {'string': ('State'), 'field': 'state'},
    {'string': ('Net Amount'), 'field': 'amount_untaxed', 'align': 'text-right', 'humanize': True},
    {'string': ('Total'), 'field': 'amount_total', 'align': 'text-right', 'humanize': True},
]

OBJECT_DETAIL_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': ('Date'), 'field': 'date_order'},
    {'string': _('Client'), 'field': 'partner_id'},
    {'string': _('Seller'), 'field': 'seller_id'},
]

OBJECT_TOTAL_FIELDS = [
    {'string': _('Net Amount or Affection:'), 'field': 'amount_untaxed'},
    {'string': _('Exempt Amount:'), 'field': 'amount_exempt'},
    {'string': _('IVA:'), 'field': 'amount_tax_iva'},
    {'string': _('Other taxes:'), 'field': 'amount_tax_other'},
    {'string': _('Total taxes:'), 'field': 'amount_tax_total'},
    {'string': _('Total:'), 'field': 'amount_total'},
]

DETAIL_OBJECT_LIST_FIELDS = [
    {'string': _('Product'), 'field': 'product_id'},
    {'string': _('Description'), 'field': 'description'},
    {'string': _('Quantity'), 'field': 'quantity', 'align': 'text-center', 'humanize': True},
    {'string': _('Invoiced'), 'field': 'invoiced_quantity', 'align': 'text-center', 'humanize': True},
    {'string': _('Delivered'), 'field': 'delivered_quantity', 'align': 'text-center', 'humanize': True},
    {'string': ('UOM'), 'field': 'uom_id', 'align': 'text-left', 'humanize': True},
    {'string': ('Price'), 'field': 'price', 'align': 'text-right', 'humanize': True},
    {'string': _('Discount'), 'field': 'discount', 'align': 'text-right', 'humanize': True},
    {'string': _('Tax'), 'field': 'tax_id'},
    {'string': _('Sub Total'), 'field': 'amount_total', 'align': 'text-right', 'humanize': True},
]

OBJECT_FORM_FIELDS = [
    {'string': _('Client'), 'field': 'partner_id'},
]

LEAD_FIELDS_SHORT = ['name', 'partner_id']


# ========================================================================== #
class PyPurchaseOrderListView(LoginRequiredMixin, FatherListView):
    """Lista de las ordenes de venta
    """
    model = PyPurchaseOrder
    # template_name = 'purchase/purchaseorderlist.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class PyPurchaseOrderDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPurchaseOrder
    template_name = 'purchase/detail.html'
    extra_context = {
        'fields': OBJECT_LIST_FIELDS,
        'master_fields': OBJECT_DETAIL_FIELDS,
        'detail_fields': DETAIL_OBJECT_LIST_FIELDS,
        'total_fields': OBJECT_TOTAL_FIELDS
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
        context['header_state_botons'] = []
        context['header_state'] = self.object.state.state
        if self.object.state.pk == 1:
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 3}
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
                        kwargs={'pk': self.object.pk, 'state': 2}
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
                        kwargs={'pk': self.object.pk, 'state': 1}
                    ),
                    'name': _('Draft'),
                    'class': ''
                }
            )
            if self.object.state.pk == 3:
                context['header_state_botons'].append(
                    {
                        'url': reverse_lazy(
                            '{}:state'.format(object_name),
                            kwargs={'pk': self.object.pk, 'state': 4}
                        ),
                        'name': _('To Invoice'),
                        'class': ''
                    }
                )
        context['print_url'] = '{}:pdf'.format(object_name)
        context['detail'] = PyPurchaseOrderDetail.objects.filter(
            active=True,
            company_id=self.request.user.active_company_id,
            purchase_order_id=self.object.pk
        )
        return context


# ========================================================================== #
class PyPurchaseOrderAddView(LoginRequiredMixin, FatherCreateView):
    """Vista para agregar las purchase
    """
    model = PyPurchaseOrder
    form_class = PyPurchaseOrderForm
    template_name = 'purchase/form.html'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = 'PyPurchaseOrder:purchase-order-add'
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['breadcrumbs'] = [
            {
                'url': '{}:list'.format(object_name),
                'name': '{}'.format(verbose_name)
            }
        ]
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
        return reverse_lazy('PyPurchaseOrder:detail', kwargs={'pk': self.object.pk})


# ========================================================================== #
class PyPurchaseOrderEditView(LoginRequiredMixin, FatherUpdateView):
    """Vista para editarar las purchase
    """
    model = PyPurchaseOrder
    form_class = PyPurchaseOrderForm
    template_name = 'purchase/form.html'
    extra_context = {'total_fields': OBJECT_TOTAL_FIELDS}

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
        context['header_state_botons'] = []
        context['header_state'] = self.object.state.state
        if self.object.state.pk == 1:
            context['header_state_botons'].append(
                {
                    'url': reverse_lazy(
                        '{}:state'.format(object_name),
                        kwargs={'pk': self.object.pk, 'state': 3}
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
                        kwargs={'pk': self.object.pk, 'state': 2}
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
                        kwargs={'pk': self.object.pk, 'state': 1}
                    ),
                    'name': _('Draft'),
                    'class': ''
                }
            )
            if self.object.state.pk == 2:
                context['header_state'][3]['class'] = 'font-weight-bold'
            if self.object.state.pk == 3:
                context['header_state_botons'].append(
                    {
                        'url': reverse_lazy(
                            '{}:state'.format(object_name),
                            kwargs={'pk': self.object.pk, 'state': 4}
                        ),
                        'name': _('To Invoice'),
                        'class': ''
                    }
                )
        # if self.object.state.pk == 4:
        #     context['header_state'][2]['class'] = 'font-weight-bold'
        context['print_url'] = '{}:pdf'.format(object_name)
        if self.request.POST:
            context['form'] = PyPurchaseOrderForm(
                self.request.POST,
                instance=self.object
            )
            context['formset'] = PRODUCT_FORMSET(
                self.request.POST,
                instance=self.object
            )
        else:
            context['form'] = PyPurchaseOrderForm(instance=self.object)
            context['formset'] = PRODUCT_FORMSET(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if self.object.state.pk == 1:
            with transaction.atomic():
                form.instance.um = self.request.user.pk
                if form.is_valid() and formset.is_valid():
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
                _('The current order %(order)s status does not allow updates.') % {'order': self.object.name}
            )
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('PyPurchaseOrder:detail', kwargs={'pk': self.object.pk})


# ========================================================================== #
class PyPurchaseOrderDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar las purchase
    """
    model = PyPurchaseOrder
    template_name = 'purchase/delete.html'
    success_url = reverse_lazy('PyPurchaseOrder:list')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = 'ELiminar Orden de Venta'
        context['action_url'] = 'PyPurchaseOrder:delete'
        context['delete_message'] = '<p>¿Está seguro de eliminar la orden de compras <strong>' + self.object.name + '</strong>?</p>'
        context['cant_delete_message'] = '<p>La orden de compras <strong>' + self.object.name + '</strong>, no puede ser eliminada.</p>'
        # context['detail'] = PyPurchaseOrderDetail.objects.filter(purchase_order_id=pk).exists()
        context['detail'] = True
        return context

    def delete(self, request, *args, **kwargs):
        # pk = self.kwargs.get(self.pk_url_kwarg)
        # self.object = self.get_object()
        # success_url = self.get_success_url()
        # detail = PyPurchaseOrderDetail.objects.filter(purchase_order_id=pk).exists()
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
def purchase_order_state(request, pk, state):
    purchase_order = PyPurchaseOrder.objects.get(pk=pk)
    state = PyPurchaseOrderState.objects.get(pk=state)
    if purchase_order.state != 4:
        with transaction.atomic():
            purchase_order.state = state
            purchase_order.save()
            if state.pk == 4:
                invoice = purchase_order_to_invoice(request, purchase_order)
                return redirect(
                    reverse_lazy(
                        'PyInvoice:detail', kwargs={
                            'pk': invoice.pk,
                            'type': 2
                        }
                    )
                )
    else:
        messages.warning(
                self.request,
                _('The current order %(order)s status does not allow updates.') % {'order': self.object.name}
            )
    return redirect(
        reverse_lazy('PyPurchaseOrder:detail', kwargs={'pk': pk})
    )


# ========================================================================== #
@login_required()
def purchase_order_to_invoice(request, purchase_order):
    # Create the invoice master
    invoice = PyInvoice.objects.create(
        uc=request.user.pk,
        company_id=purchase_order.company_id,
        partner_id=purchase_order.partner_id,
        seller_id=request.user.partner_id,
        type=2,
        purchase_order_id=purchase_order,
        amount_untaxed=purchase_order.amount_untaxed,
        amount_tax_iva=purchase_order.amount_tax_iva,
        amount_tax_other=purchase_order.amount_tax_other,
        amount_tax_total=purchase_order.amount_tax_total,
        amount_exempt=purchase_order.amount_exempt,
        amount_total=purchase_order.amount_total,
        description=purchase_order.description,
        origin=purchase_order.name,
    )

    # Create the invoice detail
    purchase_order_detail = PyPurchaseOrderDetail.objects.filter(
        purchase_order_id=purchase_order.pk
    )
    for sod in purchase_order_detail:
        invoice_detail = PyInvoiceDetail.objects.create(
            uc=request.user.pk,
            company_id=sod.company_id,
            product_id=sod.product_id,
            invoice_id=invoice,
            description=sod.description,
            quantity=sod.quantity,
            uom_id=sod.uom_id,
            price=sod.price,
            amount_untaxed=sod.amount_untaxed,
            amount_tax_iva=sod.amount_tax_iva,
            amount_tax_other=sod.amount_tax_other,
            amount_tax_total=sod.amount_tax_total,
            amount_exempt=sod.amount_exempt,
            discount=sod.discount,
            amount_total=sod.amount_total
        )

        # Create the invoice detail product m2m tax records
        invoice_detail.tax_id.set(sod.tax_id.all())
    return invoice
