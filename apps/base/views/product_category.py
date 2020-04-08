# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyProductCategory
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría Padre', 'field': 'parent_id'},
]

OBJECT_FORM_FIELDS = ['name', 'parent_id']


class ProductCategoryListView(LoginRequiredMixin, FatherListView):
    model = PyProductCategory
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ProductCategoryDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProductCategory
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ProductCategoryCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProductCategory
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductCategoryUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProductCategory
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductCategoryDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyProductCategory
    success_url = 'base:product-category'
