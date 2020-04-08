# Django Library
from django.conf.urls import url
from django.urls import path
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.views.blog import BlogView, PostDetailView
from apps.base.views.shop import WebProductDetailView, WebProductListView

# Localfolder Library
from .views.views import IndexView, UnderConstruction, contact

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='home-index'),

    path(
        'blog/',
        BlogView.as_view(
            extend_from='home/home.html',
            url_web_post='home:post',
            header_title=_("Blog")
        ),
        name='home-blog'
    ),
    path(
        'blog/post/<int:pk>/',
        PostDetailView.as_view(
            extend_from='home/home.html',
            url_web_post='home:web-blog',
            header_title=_("Blog")
        ),
        name='post'
    ),

    path(
        'shop/',
        WebProductListView.as_view(
            extend_from='home/home.html',
            url_web_product='home:web-product',
            header_title=_("Shop")
        ),
        name='web-shop'
    ),
    path(
        'shop/product/<int:pk>/',
        WebProductDetailView.as_view(
            extend_from='home/home.html',
            url_web_shop='home:web-shop',
            header_title=_("Shop")
        ),
        name='web-product'
    ),

    url(r'^license/', license, name='home-license'),
    url(r'^under-construction/', UnderConstruction, name='under-construction'),
    url(r'^contact_me$', contact, name='contact-me'),

]
