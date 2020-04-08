# Thirdparty Library
from modeltranslation.translator import TranslationOptions, register

# Localfolder Library
from .models import PyInvoiceState


@register(PyInvoiceState)
class PyInvoiceStateTranslationOptions(TranslationOptions):
    fields = ('name', 'state',)
