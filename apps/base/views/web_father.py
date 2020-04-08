# Django Library
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView, DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Thirdparty Library
# from apps.sale.models import *

# Localfolder Library
from ..forms import ActivateForm
from ..models import *


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
class FatherTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    class Meta:
        abstract = True


# ========================================================================== #
class FatherListView(ListView):
    template_name = 'base/list.html'
    EXLUDE_FROM_FILTER = (
        'PyCompany',
        'PyCountry',
        'PyCourrency',
        'PyPlugin',
        'PySequence'
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['add_url'] = reverse_lazy('{}:add'.format(object_name))
        context['form_template'] = False
        context['breadcrumbs'] = [{
            'url': False,
            'name': '{}'.format(verbose_name)
        }]
        return context

    def get_queryset(self):
        if self.model._meta.object_name in self.EXLUDE_FROM_FILTER:
            queryset = self.model.objects.filter(active=True)
        else:
            queryset = self.model.objects.filter(
                company_id=self.request.user.active_company_id,
                active=True
            )
        return queryset

    class Meta:
        abstract = True


# ========================================================================== #
class FatherDetailView(DetailView):
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['back_url'] = reverse_lazy('{}:list'.format(object_name))
        context['breadcrumbs'] = [{
            'url': reverse_lazy('{}:list'.format(object_name)),
            'name': '{}'.format(verbose_name)
        }]
        context['list_url'] = '{}:list'.format(object_name)
        context['update_url'] = reverse_lazy(
                '{}:update'.format(object_name),
                kwargs={'pk': self.object.pk}
            )
        context['delete_url'] = '{}:delete'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['form_template'] = False
        forward = self.model.objects.filter(
            pk__gt=self.kwargs['pk'],
            active=True,
            company_id=self.request.user.active_company_id
        ).first()
        backward = self.model.objects.filter(
            pk__lt=self.kwargs['pk'],
            active=True,
            company_id=self.request.user.active_company_id
        ).order_by('-pk').first()
        if forward:
            context['forward'] = reverse_lazy(
                '{}:detail'.format(object_name),
                kwargs={'pk': forward.pk}
            )
        if backward:
            context['backward'] = reverse_lazy(
                '{}:detail'.format(object_name),
                kwargs={
                    'pk': backward.pk
                }
            )
        context['activate_form'] = ActivateForm(
            initial={
                'object_name': object_name,
                'object_pk': self.kwargs['pk']
            }
        )
        return context

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = queryset.filter(
            pk=pk,
            active=True,
            company_id=self.request.user.active_company_id
        )
        queryset = queryset.filter(pk=pk)

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") %
                {'verbose_name': queryset.model._meta.verbose_name}
            )
        return obj

    class Meta:
        abstract = True


# ========================================================================== #
class FatherCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['list_url'] = '{}:list'.format(object_name)
        context['update_url'] = '{}:update'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['back_url'] = reverse_lazy('{}:list'.format(object_name))
        context['form_template'] = True
        context['breadcrumbs'] = [{
            'url': reverse_lazy('{}:list'.format(object_name)),
            'name': '{}'.format(verbose_name)
        }]

        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.uc = self.request.user.pk
        self.object.company_id = self.request.user.active_company_id
        self.object.save()
        return super().form_valid(form)

    class Meta:
        abstract = True


# ========================================================================== #
class FatherUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['list_url'] = '{}:list'.format(object_name)
        context['update_url'] = '{}:update'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['form_template'] = True
        context['back_url'] = reverse_lazy(
            '{}:detail'.format(object_name),
            kwargs={'pk': self.object.pk}
        )
        context['action_url'] = '{}:update'.format(object_name)
        if 'pk' in self.kwargs:
            forward = self.model.objects.filter(
                pk__gt=self.kwargs['pk'],
                active=True,
                company_id=self.request.user.active_company_id
            ).first()
            backward = self.model.objects.filter(
                pk__lt=self.kwargs['pk'],
                active=True,
                company_id=self.request.user.active_company_id
            ).order_by('-pk').first()
            if forward:
                context['forward'] = reverse_lazy(
                    '{}:update'.format(object_name),
                    kwargs={'pk': forward.pk}
                )
            if backward:
                context['backward'] = reverse_lazy(
                    '{}:update'.format(object_name),
                    kwargs={
                        'pk': backward.pk
                    }
                )
        context['breadcrumbs'] = [{
            'url': reverse_lazy('{}:list'.format(object_name)),
            'name': '{}'.format(verbose_name)
        }]
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.um = self.request.user.pk
        self.object.save()
        return super().form_valid(form)

    class Meta:
        abstract = True


# ========================================================================== #
class FatherDeleteView(DeleteView):
    template_name = 'base/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['title'] = _("Delete %(obj_name)s") % {"obj_name": verbose_name}
        context['delete_message'] = _("Are you sure to delete <strong>%(obj_name)s</strong>?") % {"obj_name": verbose_name}
        context['action_url'] = '{}:delete'.format(object_name)
        return context

    def get_success_url(self):
        return '{}:list'.format(self.model._meta.object_name)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy(self.get_success_url())
        eval(self.object.delete())
        return HttpResponseRedirect(success_url)

    class Meta:
        abstract = True


# ========================================================================== #
def inactive_object(request):
    if request.method == 'POST':
        form = ActivateForm(request.POST)
        if form.is_valid():
            object_name = form.cleaned_data['object_name']
            object_pk = form.cleaned_data['object_pk']
            object_to = eval(
                '{}.objects.get(pk={})'.format(object_name, object_pk)
            )
            object_to.active = False
            object_to.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


# ========================================================================== #
def active_object(request):
    if request.method == 'POST':
        form = ActivateForm(request.POST)
        if form.is_valid():
            object_name = form.cleaned_data['object_name']
            object_pk = form.cleaned_data['object_pk']
            object_to = eval(
                '{}.objects.get(pk={})'.format(object_name, object_pk)
            )
            object_to.active = True
            object_to.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
