# -*- coding: utf-8
"""
Modelo de datos de la app globales
"""
# Furture Library
from __future__ import unicode_literals

# Standard Library
import os

# Django Library
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather

# Localfolder Library
from ..models import PyPartner
from ..rename_image import RenameImage


def image_path(instance, filename):
    return os.path.join('avatar', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])


class PyUser(AbstractUser, PyFather):
    '''Modelo de los usuarios
    '''
    SEXO_CHOICES = (
        ('F', _('FEMALE')),
        ('M', _('MALE')),
    )
    LETRACEDULA_CHOICES = (
        ('V', 'V'),
        ('E', 'E'),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    password = models.CharField(_("Password"), max_length=128)
    last_login = models.DateTimeField(_("Last login"), default=timezone.now)
    is_superuser = models.BooleanField(_("Super Admin"), default=False, db_index=True)
    is_staff = models.BooleanField(_("Staff"), default=False, db_index=True)
    is_active = models.BooleanField(_("Active"), default=False)
    username = None
    first_name = models.CharField(_("Name"), max_length=30)
    last_name = models.CharField(_("Last name"), max_length=30, blank=True, null=True)
    email = models.CharField(_("Email"), max_length=254, null=False, db_index=True, unique=True)
    telefono = models.CharField(_("Phone"), max_length=255, blank=True, null=True)
    celular = models.CharField(_("Mobile Phone"), max_length=255, blank=True, null=True)
    avatar = models.ImageField(max_length=255, storage=RenameImage(), upload_to=image_path, blank=True, null=True, default='avatar/default_avatar.png')
    partner_id = models.ForeignKey(PyPartner, null=True, blank=True, on_delete=models.PROTECT)
    active_company = models.ForeignKey('base.PyCompany', on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return '%s %s' % (self.first_name, self.last_name)


    @classmethod
    def create(cls, first_name, last_name, email, password, is_superuser, is_staff, is_active, active_company):
        """Crea un partner de manera sencilla
        """
        partner_name = '{} {}'.format(first_name, last_name)
        partner = PyPartner.create(partner_name, email)
        pyuser = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            active_company=active_company,
            company_id=active_company.id,
            partner_id=partner,
        )
        pyuser.set_password(password)
        pyuser.save()

        return pyuser

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        db_table = 'auth_user'
