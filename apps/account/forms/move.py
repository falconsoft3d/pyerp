"""Formularios del modulo sale
"""
# Django Library
from django import forms
from django.forms.formsets import DELETION_FIELD_NAME
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from bootstrap_datepicker_plus import DatePickerInput
from dal import autocomplete
from taggit.forms import TagWidget

# Localfolder Library
from ..models import PyAccountMove, PyAccountMoveDetail


class MyDatePickerInput(DatePickerInput):
    template_name = 'datepicker_plus/date-picker.html'


# ========================================================================== #
class AccountMoveForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyAccountMove
        fields = [
            'journal_id',
            'date_move',
            'company_move',
            'reference'
        ]
        labels = {
            'journal_id': _('Journal',),
            'date_move': _('Date'),
            'company_move': _('Company'),
            'reference': 'Reference',
        }
        widgets = {
            'journal_id': autocomplete.ModelSelect2(
                url='PyJournal:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a journal')
                },
            ),
            'date_move': MyDatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
            'company_move': autocomplete.ModelSelect2(
                url='PyCompany:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a company'),
                    'disabled': 'true'
                },
            ),
            'reference': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('----------'),
                    # 'style': 'width: 150px',
                },
            ),
        }


class AccountMoveDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """

    class Meta:
        model = PyAccountMoveDetail
        fields = [
            'account_plan_id',
            'reference_company',
            'tags',
            'debit',
            'credit',
            'date_due'
        ]
        widgets = {
            'account_plan_id': autocomplete.ModelSelect2(
                url='PyAccountPlan:autocomplete',
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select an account'),
                },
            ),
            'reference_company': autocomplete.ModelSelect2(
                url='PyCompany:autocomplete',
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select a company'),
                },
            ),
            'tags': TagWidget(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                },
            ),
            'debit': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Debit'),
                },
            ),
            'credit': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Credit'),
                },
            ),
            'date_due': MyDatePickerInput(format='%d/%m/%Y'),
        }

    def set_index(self, index):
        self.fields['formset_index'].initial = index


class BaseAccountMoveFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''
        form.fields[DELETION_FIELD_NAME].widget = forms.HiddenInput(
            attrs={
                'value': 'false',
            },

        )


ACCOUNTING_NOTES = inlineformset_factory(
    PyAccountMove, PyAccountMoveDetail,
    form=AccountMoveDetailForm,
    formset=BaseAccountMoveFormSet,
    extra=0,
    can_delete=True
)
