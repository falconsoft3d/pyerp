# Django Library
from django.contrib import admin

# Localfolder Library
from .forms import AccountMoveDetailForm, AccountMoveForm
from .models import PyAccountMove, PyAccountMoveDetail, PyInvoiceState


class PyAccountMoveDetailInline(admin.TabularInline):
    model = PyAccountMoveDetail
    form = AccountMoveDetailForm
    extra = 0


class PyAccountMoveAdmin(admin.ModelAdmin):
    form = AccountMoveForm
    inlines = [PyAccountMoveDetailInline]


admin.site.register(PyAccountMove, PyAccountMoveAdmin)
admin.site.register(PyInvoiceState)
