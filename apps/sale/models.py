# Django Library
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather, PyPartner, PyProduct, PyTax, PyUom
from apps.base.views.sequence import get_next_value


# ========================================================================== #
class PySaleOrderState(PyFather):
    """Modelo de la orden de pago
    """
    name = models.CharField(_('Name'), max_length=80, blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Sale order state')
        verbose_name_plural = _('Sale order states')


# ========================================================================== #
class PySaleOrder(PyFather):
    """Modelo de la orden de pago
    """
    name = models.CharField(_('Name'), max_length=80, editable=False)
    partner_id = models.ForeignKey(
        PyPartner,
        on_delete=models.PROTECT,
        verbose_name=_('Client'),
    )
    seller_id = models.ForeignKey(
        PyPartner,
        on_delete=models.PROTECT,
        related_name='sale_order_seller',
        verbose_name=_('Seller'),
        null=True,
        blank=True
    )
    date_order = models.DateTimeField(default=timezone.now, null=True, blank=True)
    amount_untaxed = models.DecimalField(
        _('Amount un'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_tax_iva = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_tax_other = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_tax_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_exempt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_total = models.DecimalField(
        _('Total'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    description = models.TextField(_('Description'), blank=True, null=True)
    state = models.ForeignKey(
        PySaleOrderState,
        on_delete=models.PROTECT,
        verbose_name=_('State'),
        default=1
    )
    note = models.TextField(_('NOte'), blank=True, null=True)
    date_confirm = models.DateTimeField(null=True)

    class Meta:
        ordering = ['pk']
        verbose_name = _('Sale Order')
        verbose_name_plural = _('Sale Orders')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = get_next_value(self._meta.object_name, 'SO')

        if not self.date_order or self.date_order == "":
            self.date_order = default=timezone.now
        super().save(*args, **kwargs)


# ========================================================================== #
class PySaleOrderDetail(PyFather):
    """Modelo del detalle de la orden de pago
    """
    sale_order_id = models.ForeignKey(
        PySaleOrder,
        on_delete=models.PROTECT
    )
    product_id = models.ForeignKey(
        PyProduct,
        on_delete=models.PROTECT,
        verbose_name=_('Product')
    )
    description = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(
        _('Quantity'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    invoiced_quantity = models.DecimalField(
        _('Invoiced'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    delivered_quantity = models.DecimalField(
        _('Delivered'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    uom_id = models.ForeignKey(
        PyUom,
        verbose_name=_('UOM'),
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    tax_id = models.ManyToManyField(PyTax, verbose_name=_('Tax'), blank=True)
    amount_untaxed = models.DecimalField(
        _('Amount un'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_tax_iva = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_tax_other = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_tax_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_exempt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_total = models.DecimalField(
        _('Total'),
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ['pk']
        verbose_name = _('Sale order detail')
        verbose_name_plural = _('Sale orders detail')
