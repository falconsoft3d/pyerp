# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyWPayment
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Web Active"), 'field': 'web_active'},
]

OBJECT_FORM_FIELDS = ['name','web_active']


class WPaymentListView(LoginRequiredMixin, FatherListView):
    model = PyWPayment
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class WPaymentDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyWPayment
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class WPaymentCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyWPayment
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class WPaymentUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyWPayment
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class WPaymentDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyWPayment
