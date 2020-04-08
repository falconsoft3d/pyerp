# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..forms import PartnerForm
from ..models import PyPartner
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Street"), 'field': 'street'},
    {'string': _("Country"), 'field': 'country_id'},
    {'string': _("Phone"), 'field': 'phone'},
    {'string': _("Email"), 'field': 'email'},
    {'string': _("For Invoice"), 'field': 'for_invoice'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("No Email"), 'field': 'not_email'},
    {'string': _("Parent"), 'field': 'parent_id'},
    {'string': _("Type"), 'field': 'type'},
]

OBJECT_FORM_FIELDS = [
    'name',
    'img',
    'street',
    'country_id',
    'email',
    'phone',
    'note',
    'customer',
    'provider',
    'for_invoice',
    'not_email',
    'parent_id',
    'type',
    'active'
]


# ========================================================================== #
class CustomerListView(LoginRequiredMixin, FatherListView):
    model = PyPartner
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class ProviderListView(LoginRequiredMixin, FatherListView):
    model = PyPartner
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}
    queryset = PyPartner.objects.filter(provider=True, active=True).all()


# ========================================================================== #
class PartnerCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyPartner
    form_class = PartnerForm
    template_name = 'base/form.html'


# ========================================================================== #
class PartnerDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPartner
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class PartnerUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyPartner
    form_class = PartnerForm
    template_name = 'base/form.html'


# ========================================================================== #
class PartnerDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyPartner


# ========================================================================== #
class PartnerAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyPartner
    """
    def get_queryset(self):

        company_id = self.forwarded.get('company_id', None)

        if company_id:
            queryset = PyPartner.objects.filter(
                company_id=company_id,
                active=True
            ).order_by('name')
        else:
            queryset = PyPartner.objects.filter(active=True).order_by('name')

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
