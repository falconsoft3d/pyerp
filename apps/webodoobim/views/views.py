# Furture Library
from __future__ import unicode_literals

# Django Library
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView

BIM_PHONE = "+56 9 4299 4534"

def index(request):
    return render(request, 'webodoobim/index.html')

def about(request):
    return render(request, 'webodoobim/about.html')

def services(request):
    return render(request, 'webodoobim/services.html')

def contact(request):
    return render(request, 'webodoobim/contact_us.html')

def blog(request):
    return render(request, 'webodoobim/blog.html')
