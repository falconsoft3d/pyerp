# -*- coding: utf-8 -*-
"""
Formularios
"""
# Django Library
from django import forms
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models.product import PyProduct


class ProductForm(forms.ModelForm):
    """Fromulario para los productos
    """

    class Meta:
        model = PyProduct
        fields = [
            'name',
            'img',
            'uom_id',
            'category_id',
            'web_category_id',
            'price',
            'cost',
            'tax',
            'brand_id',
            'code',
            'bar_code',
            'type',
            'web_active',
            'pos_active',
            'description',
            'features',
            'youtube_video',
        ]
        widgets = {
            'tax': autocomplete.ModelSelect2Multiple(
                url='PyTax:autocomplete',
                attrs={
                    'data-placeholder': _('Select taxes...'),
                    'style': 'width: 100%',
                },
            ),
            'uom_id': autocomplete.ModelSelect2(
                url='PyUom:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a UOM ...'),
                    'style': 'width: 100%',
                },
            ),
            'type': forms.Select(
                attrs={
                    'class': 'static-select2',
                },
            ),
            'category_id': forms.Select(
                attrs={
                    'class': 'static-select2',
                },
            ),
            'web_category_id': forms.Select(
                attrs={
                    'class': 'static-select2',
                },
            ),
            'brand_id': forms.Select(
                attrs={
                    'class': 'static-select2',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description ...'),
                    'style': 'width: 100%',
                    'rows': '1',
                },
            ),
            'features': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Features ...'),
                    'style': 'width: 100%',
                    'rows': '1',
                },
            ),
        }
