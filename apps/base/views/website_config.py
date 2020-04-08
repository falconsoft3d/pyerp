# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Localfolder Library
from ..models.website_config import PyWebsiteConfig
from .web_father import FatherUpdateView


class UpdateWebsiteConfigView(LoginRequiredMixin, FatherUpdateView):
    model = PyWebsiteConfig
    template_name = 'base/form.html'
    fields = ['show_blog', 'show_shop', 'under_construction', 'show_chat','show_price','user_register']
