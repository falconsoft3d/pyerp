"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # ============================ New URLs ============================ #
    path('', include('apps.base.urls.usercustom')),
    path('attribute/', include('apps.base.urls.attribute')),
    path('base/', include('apps.base.urls.base')),
    path('bi/', include('apps.base.urls.bi')),
    path('channel/', include('apps.base.urls.channel')),
    path('comment/', include('apps.base.urls.comment')),
    path('company/', include('apps.base.urls.company')),
    path('country/', include('apps.base.urls.country')),
    path('cron/', include('apps.base.urls.cron')),
    path('currency/', include('apps.base.urls.currency')),
    path('faq/', include('apps.base.urls.faq')),
    path('image/', include('apps.base.urls.image')),
    path('log/', include('apps.base.urls.log')),
    path('meta/', include('apps.base.urls.meta')),
    path('page/', include('apps.base.urls.page')),
    path('parameter/', include('apps.base.urls.parameter')),
    path('partner/', include('apps.base.urls.partner')),
    path('plugin/', include('apps.base.urls.plugin')),
    path('post/', include('apps.base.urls.post')),
    path('product/', include('apps.base.urls.product')),
    path('product_brand/', include('apps.base.urls.product_brand')),
    path('product_category/', include('apps.base.urls.product_category')),
    path('product_category_uom/', include('apps.base.urls.product_category_uom')),
    path('product-webcategory/', include('apps.base.urls.product_webcategory')),
    path('sequence/', include('apps.base.urls.sequence')),
    path('shop/', include('apps.base.urls.shop')),
    path('tag/', include('apps.base.urls.tag')),
    path('tax/', include('apps.base.urls.tax')),
    path('uom/', include('apps.base.urls.uom')),
    path('variant/', include('apps.base.urls.variant')),
    path('wparameter/', include('apps.base.urls.wparameter')),
    path('wpayment/', include('apps.base.urls.wpayment')),
    path('email/', include('apps.base.urls.email')),
    path('file/', include('apps.base.urls.file')),
    path('message/', include('apps.base.urls.message')),
    path('note/', include('apps.base.urls.note')),
    path('event/', include('apps.base.urls.event')),
    path('menu/', include('apps.base.urls.menu')),
    path('api/', include('apps.base.urls.rest')),
]
