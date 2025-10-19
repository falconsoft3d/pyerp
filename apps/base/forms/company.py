# -*- coding: utf-8 -*-
"""
Formularios para Company
"""

# Django Library
from django import forms
from django.utils.translation import gettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import PyCompany


class CompanyForm(forms.ModelForm):
    """Formulario para actualizar empresa con widgets de color
    """
    
    class Meta:
        model = PyCompany
        fields = [
            'name',
            'street',
            'city',
            'phone',
            'email',
            'postal_code',
            'social_facebook',
            'social_instagram',
            'social_linkedin',
            'social_youtube',
            'social_whatsapp',
            'latitude',
            'longitude',
            'country',
            'currency_id',
            'slogan',
            'logo',
            'main_color',
            'content_wrapper_color',
            'font_color',
            'description'
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'social_facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'social_instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'social_linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'social_youtube': forms.URLInput(attrs={'class': 'form-control'}),
            'social_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': autocomplete.ModelSelect2(
                url='PyCountry:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a Country ...'),
                    'style': 'width: 100%',
                },
            ),
            'currency_id': autocomplete.ModelSelect2(
                url='PyCurrency:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a Currency ...'),
                    'style': 'width: 100%',
                },
            ),
            'slogan': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'main_color': forms.TextInput(attrs={
                'class': 'form-control color-picker',
                'type': 'color',
                'data-toggle': 'tooltip',
                'data-placement': 'top',
                'title': _('Select main color')
            }),
            'content_wrapper_color': forms.TextInput(attrs={
                'class': 'form-control color-picker',
                'type': 'color',
                'data-toggle': 'tooltip',
                'data-placement': 'top',
                'title': _('Select content wrapper color')
            }),
            'font_color': forms.TextInput(attrs={
                'class': 'form-control color-picker',
                'type': 'color',
                'data-toggle': 'tooltip',
                'data-placement': 'top',
                'title': _('Select font color')
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }
        
        labels = {
            'name': _('Company Name'),
            'street': _('Street'),
            'city': _('City'),
            'phone': _('Phone'),
            'email': _('Email'),
            'postal_code': _('Postal Code'),
            'social_facebook': _('Facebook'),
            'social_instagram': _('Instagram'),
            'social_linkedin': _('LinkedIn'),
            'social_youtube': _('YouTube'),
            'social_whatsapp': _('WhatsApp'),
            'latitude': _('Latitude'),
            'longitude': _('Longitude'),
            'country': _('Country'),
            'currency_id': _('Currency'),
            'slogan': _('Slogan'),
            'logo': _('Logo'),
            'main_color': _('Main Color'),
            'content_wrapper_color': _('Content Wrapper Color'),
            'font_color': _('Font Color'),
            'description': _('Description'),
        }