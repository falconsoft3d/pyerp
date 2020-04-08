# -*- coding: utf-8 -*-
"""
Vistas de la aplicación globales
"""

# Django Library
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView, TemplateView

# Thirdparty Library
import requests

# Localfolder Library
from ..forms import (
    AvatarForm, PasswordRecoveryForm, PasswordSetForm, PerfilForm,
    PersonaCreationForm)
from ..models import (
    PyCompany, PyMeta, PyParameter, PyPlugin, PyUser, PyWParameter)
from ..tokens import ACCOUNT_ACTIVATION_TOKEN, PASSWORD_RECOVERY_TOKEN
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)


def _count_plugin():
    return PyPlugin.objects.all().count()


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter


def _parameter():
    parameter = {}
    for parametro in PyParameter.objects.all():
        parameter[parametro.name] = parametro.value
    return parameter


def _web_meta():
    cad = ''
    for meta in PyMeta.objects.all():
        cad += '<meta name="'+meta.title+'" content="'+meta.content+'">' + '\n'
    return cad


# ========================================================================== #
class ActivateUserView(RedirectView):
    """Esta clase activa a la persona cuando confirma el link enviado desde
    su correo
    """
    url = 'PyUser:login'

    def get(self, request, *args, **kwargs):
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']
        url = self.get_redirect_url(*args, **kwargs)
        uid = force_text(urlsafe_base64_decode(uidb64))

        try:
            user = PyUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, PyUser.DoesNotExist):
            user = None

        token_valid = ACCOUNT_ACTIVATION_TOKEN.check_token(user, token)

        if user is not None and token_valid and uid != 1:
            user.is_active = True
            user.save()
            messages.success(
                self.request,
                _('Welcome, your account has been successfully activated. Please log in using your credentials.')
            )
        else:
            messages.error(
                self.request,
                _('The sign up confirm link is invalid. If your account is not yet active, use the password recovery link.')
            )

        return HttpResponseRedirect(reverse_lazy(url))


# ========================================================================== #
class AvatarUpdateView(LoginRequiredMixin, FatherUpdateView):
    """Vista para editarar las sale
    """
    model = PyUser
    form_class = AvatarForm
    success_url = reverse_lazy('PyUser:profile')

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        # pk = self.kwargs.get(self.pk_url_kwarg)
        pk = self.request.user.pk
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") %
                {'verbose_name': queryset.model._meta.verbose_name}
            )
        return obj

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        usuario = PyUser.objects.get(pk=self.request.user.pk)

        if request.method == 'POST':
            form = AvatarForm(
                self.request.POST,
                self.request.FILES,
                instance=usuario
            )
            if form.is_valid():
                form.save()

        return redirect('PyUser:profile')


# ========================================================================== #
def cambio_clave(request):
    """Esta función es para el cambio de clave del usuario
    """
    context = {}
    context['web_parameter'] = _web_parameter()
    context['parameter'] = _parameter()
    context['meta'] = _web_meta()
    context['count_plugin']= _count_plugin
    context['company'] = PyCompany.objects.filter(active=True)

    if request.method == 'POST':
        context['form'] = PasswordChangeForm(request.user, request.POST)
        if form.is_valid() and user.pk != 1:
            user = form.save()
            update_session_auth_hash(request, user)  # Importante!
            messages.success(request, _('Your password change was successfully \
                processed'))
            return redirect('PyUser:profile')
    else:
        context['form'] = PasswordChangeForm(request.user)
    return render(
        request,
        'usercustom/password_change_form.html',
        context
    )


# ========================================================================== #
class LogOutModalView(TemplateView):
    """Lista de las ordenes de venta
    """
    template_name = 'usercustom/logoutmodal.html'


# ========================================================================== #
class PasswordRecoveryView(PasswordResetView):
    """Esta Clase tiene dos funciones:
    1.- Envía un coreo al uuario con instrucciones para recuperar su
    contraseña
    2.- Despliega un formulario para recuperar la contraseña
    """
    success_url = 'PyUser:login'
    template_name = 'usercustom/password_reset_form.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'uidb64' in self.kwargs and 'token' in self.kwargs:
            # Formulario para escribir la nueva contraseña
            context['form'] = PasswordSetForm()
            context['url_action'] = reverse_lazy(
                'PyUser:password-set',
                kwargs={
                    'uidb64': self.kwargs['uidb64'],
                    'token': self.kwargs['token']
                }
            )
        else:
            # Fromulario para solicitar el link de recuperación de contraseña
            context['form'] = PasswordRecoveryForm()
            context['url_action'] = reverse_lazy('PyUser:password-recovery')

        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if 'uidb64' in self.kwargs and 'token' in self.kwargs:
            form = PasswordSetForm(request.POST)
        else:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = requests.get(url, params=values, verify=True)
            result = data.json()

            if result['success']:
                self.extra_context['reCAPTCHA_error'] = ''
            else:
                self.extra_context['reCAPTCHA_error'] = _('Invalid reCAPTCHA')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        if 'uidb64' in self.kwargs and 'token' in self.kwargs:
            uidb64 = self.kwargs['uidb64']
            token = self.kwargs['token']
            uid = force_text(urlsafe_base64_decode(uidb64))

            try:
                user = PyUser.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, PyUser.DoesNotExist):
                user = None

            token_valid = PASSWORD_RECOVERY_TOKEN.check_token(user, token)

            if user is not None and token_valid and uid != 1:
                user.set_password(form.cleaned_data['password1'])
                user.is_active = True
                user.save()
                messages.success(
                    self.request,
                    _('Welcome back, your password has been successfully modified. Please log in using your credentials.')
                )
            else:
                messages.error(
                    self.request,
                    _('The password recovery link is invalid or has already been used.')
                )

            return HttpResponseRedirect(reverse_lazy(self.get_success_url()))
        else:
            email = form.cleaned_data['email']
            try:
                user = PyUser.objects.get(email=email)
            except (TypeError, ValueError, OverflowError, PyUser.DoesNotExist):
                user = None
            if user is not None:
                current_site = get_current_site(self.request)
                subject = _('%(app_name)s password recovery') % {
                    'app_name': settings.APP_NAME
                }

                url = reverse_lazy(
                    'PyUser:password-set',
                    kwargs={
                        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': PASSWORD_RECOVERY_TOKEN.make_token(user)
                    }
                )

                message_body = _('You received this email because you requested that your password be reset to "%(app_name)s".\n\nPlease go to the following link to recover your password:\n\nhttp://%(domain)s%(url)s\n\nThe credentials of this link last for one (1) day.\n\nBest regards.\n\nThe %(app_name)s team.') % {'app_name': settings.APP_NAME, 'user': user.email, 'domain': current_site.domain, 'url': url}
                message_body = message_body.replace("  ", "")

                user.email_user(subject, message_body)

                messages.success(
                    self.request,
                    _('Instructions to recover your password in %(app_name)s were sent to the email account %(email)s') % {'app_name': settings.APP_NAME, 'email': email}
                )

                return HttpResponseRedirect(reverse_lazy(self.get_success_url()))

            else:
                messages.error(
                    self.request,
                    _('The email provided is not registered in %(app_name)s') % {
                        'app_name': settings.APP_NAME
                    }
                )

                return HttpResponseRedirect(
                    reverse_lazy('PyUser:password-recovery')
                )


# ========================================================================== #
class ProfileView(FatherUpdateView):
    """Vista para editarar las sale
    """
    model = PyUser
    form_class = PerfilForm
    template_name = 'usercustom/profile.html'
    success_message = _('Your profile was updated successfully')
    success_url = reverse_lazy('PyUser:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_avatar'] = AvatarForm(instance=self.request.user)

        return context

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        # pk = self.kwargs.get(self.pk_url_kwarg)
        pk = self.request.user.pk
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") %
                {'verbose_name': queryset.model._meta.verbose_name}
            )
        return obj


##############################################################################
class SignUpView(FatherCreateView):
    """Esta clase sirve registrar a los usuarios en el sistema
    """
    model = PyUser
    form_class = PersonaCreationForm
    template_name = 'usercustom/signup.html'
    extra_context = {}
    success_url = 'PyUser:login'
    success_message = _('Your account was created successfully. A link was sent to your email that you must sign in to confirm your sign up.')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = requests.get(url, params=values, verify=True)
        result = data.json()

        if form.is_valid() and result['success']:
            self.extra_context['reCAPTCHA_error'] = ''
            return self.form_valid(form)
        else:
            if not result['success']:
                self.extra_context['reCAPTCHA_error'] = _('Invalid reCAPTCHA')
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        self.object = form.save()
        current_site = get_current_site(self.request)
        subject = _('%(app_name)s sign up') % {'app_name': settings.APP_NAME}

        url = reverse_lazy(
            'PyUser:activar',
            kwargs={
                'uidb64': urlsafe_base64_encode(force_bytes(self.object.pk)),
                'token': ACCOUNT_ACTIVATION_TOKEN.make_token(self.object)
            }
        )

        message_body = _('Thank you for registering in %(app_name)s, your username is: %(user)s.\n\nPlease go to the following link to confirm your registration and activate your account:\n\nhttp://%(domain)s%(url)s\n\nThe credentials of this link last for one (1) day.\n\nBest regards.\n\nThe %(app_name)s team.') % {'app_name': settings.APP_NAME, 'user': self.object.email, 'domain': current_site.domain, 'url': url}
        message_body = message_body.replace("  ", "")

        self.object.email_user(subject, message_body)

        messages.success(
            self.request,
            _('Your account has been created successfully. Open the link that was sent to your email, to confirm your registration and activate your account.')
        )

        return HttpResponseRedirect(reverse_lazy(self.get_success_url()))
