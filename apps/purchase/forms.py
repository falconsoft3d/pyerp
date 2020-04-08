"""Formularios del modulo purchase
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
from .models import PyPurchaseOrder, PyPurchaseOrderDetail


class MyDatePickerInput(DatePickerInput):
    template_name = 'datepicker_plus/date-picker.html'


# ========================================================================== #
class PyPurchaseOrderForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyPurchaseOrder
        fields = [
            'date_order',
            'partner_id',
            'seller_id',
            'note',
            'company_id'
        ]
        widgets = {
            'partner_id': autocomplete.ModelSelect2(
                url='PyPartner:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Choose a provider ...'),
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
            'date_order': MyDatePickerInput(
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
                    'placeholder': _('Description ...'),
                    'style': 'width: 100%',
                },
            ),
            'company_id': forms.HiddenInput(),
        }


class PyPurchaseOrderDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyPurchaseOrderDetail
        exclude = ()
        fields = [
            'product_id',
            'description',
            'quantity',
            'invoiced_quantity',
            'delivered_quantity',
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
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select a product ...'),
                    'style': 'width: 180px',
                },
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                },
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('Product quantity ...'),
                },
            ),
            'invoiced_quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('Invoiced ...'),
                    'readonly': True,
                },
            ),
            'delivered_quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('Delivered'),
                    'readonly': True,
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
                    'class': 'form-control form-control-sm text-right',
                    'placeholder': 'Precio del producto ...',
                    # 'style': 'width: 80px',
                    'value': 0,
                },
            ),
            'discount': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm text-right',
                    'placeholder': 'Descuento ...',
                    # 'style': 'width: 80px',
                },
            ),
            'tax_id': autocomplete.ModelSelect2Multiple(
                url='PyTax:autocomplete',
                attrs={
                    'class': 'form-control  custom-select custom-select-sm',
                    'data-placeholder': _('Select taxes...'),
                    'style': 'width: 280px',
                },
            ),
            'amount_total': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm text-right',
                    'placeholder': 'Total ...',
                    # 'style': 'width: 80px',
                    'readonly': True,
                },
            ),
        }


class BaseProductFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''
        form.fields[DELETION_FIELD_NAME].widget = forms.HiddenInput(
            attrs={
                'value': 'false',
            },

        )


PRODUCT_FORMSET = inlineformset_factory(
    PyPurchaseOrder, PyPurchaseOrderDetail,
    form=PyPurchaseOrderDetailForm,
    formset=BaseProductFormSet,
    extra=0,
    can_delete=True
)
