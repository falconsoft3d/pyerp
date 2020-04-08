# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..forms.product import ProductForm
from ..models import PyProduct
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Code"), 'field': 'code'},
    {'string': _("Bar Code"), 'field': 'bar_code'},
    {'string': _("Name"), 'field': 'name'},
    {'string': _("UOM"), 'field': 'uom_id'},
    {'string': _("Tax"), 'field': 'tax'},
    {'string': _("Category"), 'field': 'category_id'},
    {'string': _("Brand"), 'field': 'brand_id'},
    {'string': _("Web Category"), 'field': 'web_category_id'},
    {'string': _("Price"), 'field': 'price'},
    {'string': _("Cost"), 'field': 'cost'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Youtube Video"), 'field': 'youtube_video'},
]

OBJECT_FORM_FIELDS = [
    'name',
    'uom_id',
    'category_id',
    'tax',
    'web_category_id',
    'brand_id',
    'code',
    'bar_code',
    'price',
    'cost',
    'type',
    'web_active',
    'pos_active',
    'share',
    'featured',
    'img',
    'youtube_video',
    'description',
    'company_id',
]


# ========================================================================== #
class ProductListView(LoginRequiredMixin, FatherListView):
    model = PyProduct
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class ProductDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProduct
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class ProductCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProduct
    form_class = ProductForm
    template_name = 'base/form.html'


# ========================================================================== #
class ProductUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProduct
    form_class = ProductForm
    template_name = 'base/form.html'


# ========================================================================== #
class ProductDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyProduct


# ========================================================================== #
class ProductAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        queryset = PyProduct.objects.filter(active=True)

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
