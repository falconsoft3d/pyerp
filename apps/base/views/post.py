# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.post import PyPost
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
            {'string': _("Title"), 'field': 'title'},
            {'string': _("Created on"), 'field': 'created_on'},
            {'string': _("Keywords"), 'field': 'keywords'},

        ]

OBJECT_FORM_FIELDS = ['title', 'keywords', 'content', 'img', ]


# ========================================================================== #
class PostListView(LoginRequiredMixin, FatherListView):
    model = PyPost
    template_name = 'base/list.html'


# ========================================================================== #
class PostDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPost
    template_name = 'base/detail.html'


# ========================================================================== #
class PostCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyPost
    fields = OBJECT_FORM_FIELDS


# ========================================================================== #
class PostUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyPost
    fields = OBJECT_FORM_FIELDS


# ========================================================================== #
class PostDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyPost
    success_url = 'base:post-backend'
