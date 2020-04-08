"""Formularios del modulo invoice
"""
# Django Library
from django import forms
from django.forms.formsets import DELETION_FIELD_NAME
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from bootstrap_datepicker_plus import DatePickerInput
from dal import autocomplete

# Localfolder Library
from ..models import PyInvoice, PyInvoiceDetail


class MyDatePickerInput(DatePickerInput):
    template_name = 'datepicker_plus/date-picker.html'


# ========================================================================== #
class InvoiceForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyInvoice
        fields = [
            'date_invoice',
            'partner_id',
            'seller_id',
            'note',
            'company_id',
            'origin',
            'type'
        ]
        widgets = {
            'partner_id': autocomplete.ModelSelect2(
                url='PyPartner:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un cliente ...',
                    'style': 'width: 100%',
                },
            ),
            'seller_id': autocomplete.ModelSelect2(
                url='PyPartner:autocomplete',
                forward=['company_id'],
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Choose a seller ...'),
                    'style': 'width: 100%',
                },
            ),
            'date_invoice': MyDatePickerInput(
                options={
                    "format": "DD/MM/YYYY HH:mm",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Invoice notes ...'),
                    'style': 'width: 100%',
                    'rows': '1',
                },
            ),
            'company_id': forms.HiddenInput(),
            'type': forms.HiddenInput(),
            'origin': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Origin'
                },
            ),
        }


# ========================================================================== #
class SaleOrderDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyInvoiceDetail
        exclude = ()
        fields = [
            'product_id',
            'description',
            'quantity',
            'uom_id',
            'price',
            'discount',
            'tax_id',
            'amount_total',
        ]
        widgets = {
            'product_id': autocomplete.ModelSelect2(
                url='PyProduct:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a product ...'),
                },
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('----------'),
                },
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Product quantity ...'),
                },
            ),
            'uom_id': autocomplete.ModelSelect2(
                url='PyUom:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a UOM ...'),
                },
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control text-right',
                    'data-placeholder': 'Precio del producto ...',
                    'value': 0,
                },
            ),
            'discount': forms.NumberInput(
                attrs={
                    'class': 'form-control text-right',
                    'data-placeholder': 'Descuento ...',
                },
            ),
            'tax_id': autocomplete.ModelSelect2Multiple(
                url='PyTax:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select taxes...'),
                },
            ),
            'amount_total': forms.TextInput(
                attrs={
                    'class': 'form-control text-right',
                    'data-placeholder': 'Total ...',
                    'readonly': True,
                    'style': 'width: 6.5em;',
                },
            ),
        }


class BaseProductFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''
        form.fields[DELETION_FIELD_NAME].widget = forms.HiddenInput(
            attrs={'value': 'false',},
        )


PRODUCT_FORMSET = inlineformset_factory(
    PyInvoice, PyInvoiceDetail,
    form=SaleOrderDetailForm,
    formset=BaseProductFormSet,
    extra=0,
    can_delete=True
)
