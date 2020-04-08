# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import PyCompany, PyUser
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Street"), 'field': 'street'},
    {'string': _("Phone"), 'field': 'phone'},
    {'string': _("Email"), 'field': 'email'},
    {'string': _("Country"), 'field': 'country'},
    {'string': _("Currency"), 'field': 'currency_id'},
    {'string': _("Slogan"), 'field': 'slogan'},
    {'string': _("Postal Code"), 'field': 'postal_code'},
]

OBJECT_FORM_FIELDS = [
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


# ========================================================================== #
class CompanyListView(LoginRequiredMixin, FatherListView):
    model = PyCompany
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class CompanyDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyCompany
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class CompanyCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyCompany
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


# ========================================================================== #
class CompanyUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyCompany
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


# ========================================================================== #
@login_required()
def change_active_company(request, company):
    user = PyUser.objects.get(pk=request.user.pk)
    user.active_company = PyCompany.objects.get(pk=company)
    user.save()
    return redirect(request.META.get('HTTP_REFERER'))


# ========================================================================== #
class CompanyDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyCompany


# ========================================================================== #
class CompanyAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        queryset = PyCompany.objects.filter(active=True)

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
