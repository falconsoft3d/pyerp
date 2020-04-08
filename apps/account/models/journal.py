# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather

# Localfolder Library
from .plan import PyAccountPlan

JOURNAL_TYPE = (
        ("sale", _("Sale")),
        ("purchase", _("Purchase")),
        ("cash", _("Cash")),
        ("bank", _("bank")),
        ("miscellaneous", _("Miscellaneous")),
    )


# ========================================================================== #
class PyJournal(PyFather):
    name = models.CharField(_("Name"), max_length=80)
    type = models.CharField(
        choices=JOURNAL_TYPE,
        max_length=13,
        default='Sale'
    )
    short_code = models.CharField(max_length=6)
    default_credit_account = models.ForeignKey(
        PyAccountPlan,
        verbose_name=_("Default Credit Account"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='credit_acount'
    )
    default_debit_account = models.ForeignKey(
        PyAccountPlan,
        verbose_name=_("Default Debit Account"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='debit_account'
    )

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('PyJournal:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("Journal")
        verbose_name_plural = _("Journals")
