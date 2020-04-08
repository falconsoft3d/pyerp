# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import router, transaction
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import PySequence
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Prefix"), 'field': 'prefix'},
    {'string': _("Padding"), 'field': 'padding'},
    {'string': _("Initial"), 'field': 'initial'},
    {'string': _("Increment"), 'field': 'increment'},
    {'string': _("Reset"), 'field': 'reset'},
    {'string': _("Next"), 'field': 'next_val'},
]

OBJECT_FORM_FIELDS = ['name', 'prefix', 'padding', 'initial', 'increment', 'reset', 'next_val']


class SequenceListView(LoginRequiredMixin, FatherListView):
    model = PySequence
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class SequenceDetailView(LoginRequiredMixin, FatherDetailView):
    model = PySequence
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class SequenceCreateView(LoginRequiredMixin, FatherCreateView):
    model = PySequence
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class SequenceUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PySequence
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


# ========================================================================== #
class SequenceDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PySequence
    success_url = 'base:sequences'


# ========================================================================== #
def get_next_value(name='default', prefix='default', padding=4, initial=1, increment=1, reset=None, *, nowait=False, using=None):
    """
    Return the next value for a given sequence.
    """
    if reset is not None:
        assert initial < reset

    if using is None:
        using = router.db_for_write(PySequence)

    with transaction.atomic(using=using, savepoint=False):
        sequence, created = (
            PySequence.objects.select_for_update(
                nowait=nowait
            ).get_or_create(
                name=name,
                defaults={
                    'prefix': prefix,
                    'padding': padding,
                    'initial': initial,
                    'increment': increment,
                    'reset': reset,
                    'last': initial,
                    'next_val': initial + 1
                }
            )
        )
        if not created:
            if (sequence.last + 1) != sequence.next_val:
                sequence.last = sequence.next_val
            else:
                sequence.last += increment

            sequence.next_val = sequence.last + 1

            if reset is not None and sequence.last >= reset:
                sequence.last = initial

            sequence.save()
        return '{}{}'.format(prefix, str(sequence.last).zfill(padding))
