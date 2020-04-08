""" Account Plans model
"""
# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather, PyTax
from taggit.managers import TaggableManager

ACCOUNT_PLAN_TYPE = (
    ("To Charge", _("To Charge")),
    ("To Pay", _("To Pay")),
    ("Bank and Cashier", _("Bank and Cashier")),
    ("Credit Card", _("Credit Card")),
    ("Current Assets", _("Current Assets")),
    ("Non-current Assets", _("Non-current Assets")),
    ("Pre-payments", _("Pre-payments")),
    ("Fixed Assets", _("Fixed Assets")),
    ("Current Liability", _("Current Liability")),
    ("Non-current Liabilities", _("Non-current Liabilities")),
    ("Capital", _("Capital")),
    ("Current Year Earnings", _("Current Year Earnings")),
    ("Other Income", _("Other Income")),
    ("Income", _("Income")),
    ("Depreciation", _("Depreciation")),
    ("Expenses", _("Expenses")),
    ("Direct Cost of Sales", _("Direct Cost of Sales")),
    ("Unclassified Accounts", _("Unclassified Accounts")),
)


# ========================================================================== #
class PyAccountPlan(PyFather):
    code = models.CharField(_('Code'), max_length=80)
    name = models.CharField(_('Name'), max_length=80)
    type = models.CharField(
        choices=ACCOUNT_PLAN_TYPE,
        max_length=64,
        default='activo'
    )
    tax_id = models.ManyToManyField(PyTax, verbose_name=_('Tax'), blank=True)
    reconcile = models.BooleanField(_("Reconcile"), default=False)
    tags = TaggableManager(blank=True)
    discontinued = models.BooleanField(_("Discontinued"), default=False)

    def get_absolute_url(self):
        return reverse('PyAccountPlan:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "[{}] {}".format(self.code, self.name)

    class Meta:
        verbose_name = _("Account Plan")
        verbose_name_plural = _("Account Plans")
