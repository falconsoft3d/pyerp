# Django Library
from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'apps.base'
    default_auto_field = 'django.db.models.BigAutoField'
