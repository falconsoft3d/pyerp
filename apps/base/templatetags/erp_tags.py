
"""
"""
# Django Library
from django import template
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyWebsiteConfig

# Localfolder Library
from ..models import PyPlugin
from ..models.base_config import BaseConfig

register = template.Library()


@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter
def get_online(obj):
    try:
        return BaseConfig.objects.get(pk=1).online
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_name(obj):
    try:
        if BaseConfig.objects.get(pk=1).main_company_id:
            return BaseConfig.objects.get(pk=1).main_company_id.name
        else:
            return _('Your Company Name')
    except BaseConfig.DoesNotExist:
        return _('Your Company Name')


@register.filter
def get_company_logo(obj):
    try:
        if BaseConfig.objects.get(pk=1).main_company_id:
            return BaseConfig.objects.get(pk=1).main_company_id.logo
        else:
            return 'logo/default_logo.png'
    except BaseConfig.DoesNotExist:
        return 'logo/default_logo.png'


@register.filter
def get_company_email(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.email
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_slogan(obj):
    try:
        if BaseConfig.objects.get(pk=1).main_company_id:
            return BaseConfig.objects.get(pk=1).main_company_id.slogan
        else:
            return _('Your Company Slogan')
    except BaseConfig.DoesNotExist:
        return _('Your Company Slogan')



@register.filter
def get_company_rut(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.rut
    except BaseConfig.DoesNotExist:
        return None



@register.filter
def get_company_facebook(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_facebook
    except BaseConfig.DoesNotExist:
        return None



@register.filter
def get_company_instagram(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_instagram
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_linkedin(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_linkedin
    except BaseConfig.DoesNotExist:
        return None

@register.filter
def get_company_whatsapp(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_whatsapp
    except BaseConfig.DoesNotExist:
        return None

@register.filter
def currency_symbol(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.currency_id.symbol


@register.filter
def currency_position(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.currency_id.position


@register.filter
def get_app_list(obj):
    apps = PyPlugin.objects.all().filter(installed=True).order_by('sequence')
    return [app.name.lower() + "/menu.html" for app in apps]

@register.filter
def web_chat(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_chat
    except PyWebsiteConfig.DoesNotExist:
        return None



@register.filter
def web_show_shop(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_shop
    except PyWebsiteConfig.DoesNotExist:
        return None



@register.filter
def web_under_construction(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).under_construction
    except PyWebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_blog(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_blog
    except PyWebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_price(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_price
    except PyWebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_register_user(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).user_register
    except PyWebsiteConfig.DoesNotExist:
        return None
