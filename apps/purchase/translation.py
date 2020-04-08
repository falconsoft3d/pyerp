# Thirdparty Library
from modeltranslation.translator import TranslationOptions, register

# Localfolder Library
from .models import PyPurchaseOrderState


@register(PyPurchaseOrderState)
class PyPurchaseOrderStateTranslationOptions(TranslationOptions):
    fields = ('name', 'state',)
