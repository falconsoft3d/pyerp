"""
Sección administrativa
"""
# Django Library
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

# Localfolder Library
from .forms import PersonaChangeForm, PersonaCreationForm
from .models import (
    PyCompany, PyCountry, PyPartner, PyPlugin, PyProduct, PyProductCategory,
    PyUser, PyWebsiteConfig, PyWPayment)
from .models.base_config import BaseConfig

admin.site.register(PyWebsiteConfig)

admin.site.register(PyWPayment)
admin.site.register(PyPartner)
admin.site.register(PyProduct)
admin.site.register(PyCountry)
admin.site.register(PyProductCategory)
admin.site.register(PyCompany)
admin.site.register(PyPlugin)
admin.site.register(Permission)
admin.site.register(BaseConfig)


class PersonaAdmin(UserAdmin):
    """ Admin para usuarios
    """
    form = PersonaChangeForm
    add_form = PersonaCreationForm
    # fieldsets = (
    #     ('Usuario', {
    #         'fields': ('username',
    #                    'email')
    #     }),
    #     ('Información personal', {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'first_name',
    #             'last_name',
    #             'email',
    #         ),
    #     }),
    #     ('Permisos', {
    #         'classes': ('collapse',),
    #         'fields': ('is_superuser',
    #                    'is_staff',
    #                    'is_active',
    #                    'password',
    #                    'groups',
    #                    'user_permissions'),
    #     }),
    #     ('Auditoria', {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'last_login',
    #             'date_joined',),
    #     }),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username',
    #                    'email',
    #                    'password1',
    #                    'password2',)}
    #      ),
    # )

    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser')
    list_display = ('__str__', 'email',)
    # list_select_related = ()
    show_full_result_count = False
    actions_selection_counter = False
    ordering = ('id',)

    # def get_search_results(self, request, queryset, search_term):
    #   queryset, use_distinct = super(PersonaAdmin, self).get_search_results(
    #         request, queryset, search_term)
    #     try:
    #         search_term_as_int = int(search_term)
    #     except ValueError:
    #         pass
    #     else:
    #         queryset = self.model.objects.filter(
    #             cedulaidentidad=search_term_as_int)
    #     return queryset, use_distinct

admin.site.register(PyUser, PersonaAdmin)


admin.site.register(LogEntry)
