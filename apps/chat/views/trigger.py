# Django Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Localfolder Library
from ..models.trigger import PyTrigger

TRIGGER_FIELDS = [
    {'string': _('Question'), 'field': 'question'},
    {'string': _('Answer'), 'field': 'answer'},
    {'string': _('Init'), 'field': 'init'},
]

TRIGGER_SHORT = ['question','answer','init']



class TriggerListView(LoginRequiredMixin, ListView):
    model = PyTrigger
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TriggerListView, self).get_context_data(**kwargs)
        context['title'] = 'Trigger'
        context['detail_url'] = 'base:trigger-detail'
        context['add_url'] = 'base:trigger-add'
        context['fields'] = TRIGGER_FIELDS
        return context


class TriggerDetailView(LoginRequiredMixin, DetailView):
    model = PyTrigger
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TriggerDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].question
        context['breadcrumbs'] = [{'url': 'base:triggers', 'name': 'Triggers'}]
        context['update_url'] = 'base:trigger-update'
        context['delete_url'] = 'base:trigger-delete'
        context['fields'] = TRIGGER_FIELDS
        return context


class TriggerCreateView(LoginRequiredMixin, CreateView):
    model = PyTrigger
    fields = TRIGGER_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TriggerCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Trigger'
        context['breadcrumbs'] = [{'url': 'base:triggers', 'name': 'Triggers'}]
        context['back_url'] = reverse('base:triggers')
        return context


class TriggersUpdateView(LoginRequiredMixin, UpdateView):
    model = PyTrigger
    fields = TRIGGER_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TriggersUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].question
        context['breadcrumbs'] = [{'url': 'base:triggers', 'name': 'Triggers'}]
        context['back_url'] = reverse('base:trigger-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteTrigger(self, pk):
    trigger = PyTrigger.objects.get(id=pk)
    trigger.delete()
    return redirect(reverse('base:triggers'))
