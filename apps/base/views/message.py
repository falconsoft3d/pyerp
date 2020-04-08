# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PyMessage
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Message"), 'field': 'message'},
]

OBJECT_FORM_FIELDS = ['message', 'user_id']


class MessageListView(LoginRequiredMixin, FatherListView):
    model = PyMessage
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class MessageDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyMessage
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class MessageCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyMessage
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class MessageUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyMessage
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class MessageDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyMessage
    success_url = 'base:messages'
