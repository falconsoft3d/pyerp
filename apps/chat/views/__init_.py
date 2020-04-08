# Standard Library
import datetime
import json

# Django Library
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render

# Localfolder Library
from ..models.visitor import PyChatHistory, PyVisitor


@login_required(login_url="base:login")
def chat_home(request):
    return render(request, "pychat.html")


def get_client_name(self, sid):
    visitor = PyVisitor.objects.filter(sid=sid).first()
    return HttpResponse(json.dumps({
        'name': visitor and visitor.name or 'No registrado %s' % sid[-5:]
    }), content_type='application/json')


def get_by_sid(self, sid):
    return PyVisitor.objects.filter(sid=sid).first()


def register_message(self, **kwargs):
    sid = kwargs.get('sid')
    message = kwargs.get('message')
    date = datetime.datetime.strptime(kwargs.get('date'), '%Y-%m-%d %H:%M:%S')
    visitor = PyVisitor.objects.filter(sid=sid).first()
    if not visitor:
        visitor = PyVisitor(sid=sid)
        visitor.save()
    chat_message = PyChatHistory(visitor=visitor, message=message, datetime=date, response=kwargs.get('response'))
    chat_message.save()
    return HttpResponse(b'Ok')


def get_history(self, sid):
    visitor = PyVisitor.objects.filter(sid=sid).first()
    history = PyChatHistory.objects.filter(visitor=visitor)
