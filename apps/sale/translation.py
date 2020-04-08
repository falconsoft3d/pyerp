# Thirdparty Library
from modeltranslation.translator import TranslationOptions, register

# Localfolder Library
from .models import PySaleOrderState


@register(PySaleOrderState)
class PySaleOrderStateTranslationOptions(TranslationOptions):
    fields = ('name', 'state')
