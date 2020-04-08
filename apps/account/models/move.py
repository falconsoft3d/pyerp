# Standard Library
# Django Library
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyCompany, PyFather
from apps.base.views.sequence import get_next_value
from taggit.managers import TaggableManager

# Localfolder Library
from .journal import PyJournal
from .plan import PyAccountPlan

ACCOUNT_MOVE_STATE = (
        (0, _('No asentado')),
        (1, _('Validado')),
        (2, _('cancel')),
        (3, _('confirmed'))
    )


# ========================================================================== #
class PyAccountMove(PyFather):
    name = models.CharField(_('Name'), max_length=80)
    state = models.IntegerField(
        _('Status'),
        choices=ACCOUNT_MOVE_STATE,
        default=0
    )
    journal_id = models.ForeignKey(PyJournal, on_delete=models.PROTECT)
    date_move = models.DateField(default=timezone.now)
    company_move = models.ForeignKey(
        PyCompany,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    reference = models.CharField(
        _('Reference'),
        max_length=80,
        null=True,
        blank=True
    )
    amount = models.DecimalField(
        _('Total'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    debit = models.DecimalField(
        _('debit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    credit = models.DecimalField(
        _('credit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):
        self.name = get_next_value(self._meta.object_name, 'ACC')

        if not self.date_move or self.date_move == "":
            self.date_move = timezone.now
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('PyAccountMove:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = _("Account Move")
        verbose_name_plural = _("Account Moves")


# ========================================================================== #
class PyAccountMoveDetail(PyFather):
    """Modelo del detalle de la orden de pago
    """
    name = models.CharField(_('Name'), max_length=80)
    account_move_id = models.ForeignKey(
        PyAccountMove,
        on_delete=models.PROTECT,
        verbose_name=_('account')
    )
    account_plan_id = models.ForeignKey(
        PyAccountPlan,
        on_delete=models.PROTECT
    )
    reference_company = models.ForeignKey(
        PyCompany,
        on_delete=models.PROTECT,
        verbose_name=_('company')
    )
    tags = TaggableManager(blank=True, verbose_name=_('tag'))
    debit = models.DecimalField(
        _('debit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    credit = models.DecimalField(
        _('credit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    date_due = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = get_next_value(self._meta.object_name, 'ACN')

        if not self.date_due or self.date_due == "":
            self.date_due = timezone.now
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['pk']
        verbose_name = _('Account Move detail')
        verbose_name_plural = _('Account Move details')
