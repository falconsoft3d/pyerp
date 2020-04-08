"""Signals para el calculo de las ordenes de compra
"""

# Django Library
from django.db.models.signals import post_save
from django.dispatch import receiver

# Thirdparty Library
from apps.purchase.models import PyPurchaseOrder, PyPurchaseOrderDetail


# ========================================================================== #
@receiver(post_save, sender=PyPurchaseOrder)
def calc_purchase_order(sender, instance, **kwargs):
    amount_untaxed = 0
    amount_exempt = 0
    amount_tax_iva = 0
    amount_tax_other = 0

    t_amount_untaxed = 0
    t_amount_exempt = 0
    t_amount_tax_iva = 0
    t_amount_tax_other = 0
    t_amount_tax_total = 0

    amount_total = 0

    for product in PyPurchaseOrderDetail.objects.filter(purchase_order_id=instance.pk):
        amount_untaxed = (product.quantity * product.price) - product.discount
        if product.tax_id.all().exists():
            for tax in product.tax_id.all():
                if tax.pk == 1:
                    amount_tax_iva = (amount_untaxed * tax.amount)/100
                else:
                    amount_tax_other += (amount_untaxed * tax.amount)/100
        else:
            amount_exempt = amount_untaxed
        product.active = True
        product.company_id = instance.company_id
        product.amount_untaxed = amount_untaxed
        product.amount_tax_iva = amount_tax_iva
        product.amount_tax_other = amount_tax_other
        product.amount_tax_total = amount_tax_iva + amount_tax_other
        product.amount_exempt = amount_exempt
        product.amount_total = amount_untaxed + amount_tax_iva + amount_tax_other
        product.save()

        t_amount_untaxed += product.amount_untaxed
        t_amount_tax_iva += product.amount_tax_iva
        t_amount_tax_other += product.amount_tax_other
        t_amount_tax_total += product.amount_tax_total
        t_amount_exempt += product.amount_exempt
        amount_total += product.amount_total

        amount_untaxed = 0
        amount_exempt = 0
        amount_tax_iva = 0
        amount_tax_other = 0

    instance.amount_untaxed = t_amount_untaxed
    instance.amount_tax_iva = t_amount_tax_iva
    instance.amount_tax_other = t_amount_tax_other
    instance.amount_tax_total = t_amount_tax_total
    instance.amount_exempt = t_amount_exempt
    instance.amount_total = amount_total
