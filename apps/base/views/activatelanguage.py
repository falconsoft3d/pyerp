# -*- coding: utf-8 -*-
"""
Vistas de la aplicación globales
"""

# Standard Library
from urllib.parse import urlparse

# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.utils import translation
from django.views.generic.base import View


# ========================================================================== #
class ActivateLanguageView(LoginRequiredMixin, View):
    ''' Clase para la activación de un lenguaje
    '''
    language_code = ''
    redirect_from = ''
    redirect_to = ''
    match = ''

    def get(self, request, *args, **kwargs):
        ''' Metodo para hacer switch en idiomas
        '''
        self.redirect_from = request.META.get('HTTP_REFERER', None) or '/'
        self.match = resolve(urlparse(self.redirect_from)[2])
        self.language_code = kwargs.get('language_code')
        self.redirect_to = self.match.namespace + ':' + self.match.url_name
        # self.redirect_to = self.match.url_name
        translation.activate(self.language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = self.language_code

        return redirect(reverse(self.redirect_to, kwargs=self.match.kwargs))
