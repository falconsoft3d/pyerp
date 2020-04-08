# Furture Library
from __future__ import unicode_literals

# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Localfolder Library
from ..models import PyProduct, PyWParameter
from .web_father import FatherDetailView, FatherListView

# Tienda de Productos

OBJECT_LIST_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Descripción', 'field': 'description'},
    {'string': 'Precio', 'field': 'price'},
    {'string': 'Activo', 'field': 'web_active'},
    {'string': 'Código', 'field': 'code'},
    {'string': 'Código Barra', 'field': 'code'},
]


class WebProductListView(LoginRequiredMixin, FatherListView):
    """ Despleiga todos los poductos de la tienda con la posibilidad de
    filtralos por categoria
    """
    model = PyProduct
    template_name = 'shop/shop.html'
    fields = OBJECT_LIST_FIELDS
    paginate_by = 8
    extend_from = None
    url_web_product = None
    header_title = None
    queryset = PyProduct.objects.filter(web_active='True', active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extend_from'] = self.extend_from
        context['url_web_product'] = self.url_web_product
        context['header_title'] = self.header_title
        return context


class WebProductDetailView(LoginRequiredMixin, FatherDetailView):
    """Detalle del producto
    """
    model = PyProduct
    template_name = 'shop/product.html'
    extend_from = None
    url_web_shop = None
    header_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extend_from'] = self.extend_from
        context['url_web_shop'] = self.url_web_shop
        context['header_title'] = self.header_title
        return context
