# Django Library
from django.conf.urls import url
from django.urls import path

# Localfolder Library
from .views.views import about, blog, contact, index, services

app_name = 'webodoobim'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'about/', about, name='about'),
    url(r'services/', services, name='services'),
    url(r'contact/', contact, name='contact'),
    url(r'blog/', blog, name='blog'),

]
