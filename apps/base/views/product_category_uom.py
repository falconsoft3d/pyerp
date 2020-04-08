# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyProductCategoryUOM
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': 'Name', 'field': 'name'},
]

OBJECT_FORM_FIELDS = ['name']


class ProductCategoryUOMListView(LoginRequiredMixin, FatherListView):
    model = PyProductCategoryUOM
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ProductCategoryUOMDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProductCategoryUOM
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ProductCategoryUOMCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProductCategoryUOM
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductCategoryUOMUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProductCategoryUOM
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductCategoryUOMDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyProductCategoryUOM
