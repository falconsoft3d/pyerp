# Furture Library
from __future__ import unicode_literals

# Django Library
from django.core import serializers
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView, TemplateView

# Thirdparty Library
from apps.base.models import PyPartner, PyProduct, PyWParameter
from apps.base.views.web_father import FatherTemplateView

# from apps.crm.submodels.lead import PyLead


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter


class IndexView(FatherTemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        return context



def index(request):
    web_parameter = {}
    context['web_parameter'] = _web_parameter()
    return render(request, 'home/index.html', web_parameter)

def post(request):
    context['web_parameter'] = _web_parameter()
    return render(request, 'home/post.html')

def license(request):
    context['web_parameter'] = _web_parameter()
    return render(request, 'home/license.html')

def UnderConstruction(request):
    context['web_parameter'] = _web_parameter()
    return render(request, 'home/under_construction.html')


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    partners = PyPartner.objects.filter(email=email)
    send = True
    if partners:
        partner = partners[0]
        if partner.not_email:
            send = False
    else:
        partner = PyPartner(name=name, email=email, phone=phone)
        partner.save()

    if send:
        title = name
        # lead = PyLead(name=title, content=message, partner_id=partner)
        # lead.save()
        body = render_to_string('home/contact_mail_template.html', {'name': name, 'phone': phone, 'message': message})
        email_message = EmailMessage(subject='Mensaje de usuario', body=body, from_email=email, to=['mfalcon@ynext.cl'])
        email_message.content_subtype = 'html'
        email_message.send()
        return HttpResponse(content='OK')
