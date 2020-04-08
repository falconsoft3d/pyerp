"""Signals para el calculo de las ordenes de compra
"""

# Django Library
from django.db.models.signals import post_save
from django.dispatch import receiver

# Localfolder Library
from .models import (
    PyAccountMove, PyAccountMoveDetail, PyInvoice, PyInvoiceDetail)


# ========================================================================== #
@receiver(post_save, sender=PyInvoice)
def calc_invoice(sender, instance, **kwargs):
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

    for obj in PyInvoiceDetail.objects.filter(invoice_id=instance.pk):
        amount_untaxed = (obj.quantity * obj.price) - obj.discount
        if obj.tax_id.all().exists():
            for tax in obj.tax_id.all():
                if tax.pk == 1:
                    amount_tax_iva = (amount_untaxed * tax.amount)/100
                else:
                    amount_tax_other += (amount_untaxed * tax.amount)/100
        else:
            amount_exempt = amount_untaxed
        obj.active = True
        obj.company_id = instance.company_id
        obj.amount_untaxed = amount_untaxed
        obj.amount_tax_iva = amount_tax_iva
        obj.amount_tax_other = amount_tax_other
        obj.amount_tax_total = amount_tax_iva + amount_tax_other
        obj.amount_exempt = amount_exempt
        obj.amount_total = amount_untaxed + amount_tax_iva + amount_tax_other
        obj.save()

        t_amount_untaxed += obj.amount_untaxed
        t_amount_tax_iva += obj.amount_tax_iva
        t_amount_tax_other += obj.amount_tax_other
        t_amount_tax_total += obj.amount_tax_total
        t_amount_exempt += obj.amount_exempt
        amount_total += obj.amount_total

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


# ========================================================================== #
@receiver(post_save, sender=PyAccountMove)
def calc_account_move(sender, instance, **kwargs):
    t_adebit = 0
    t_credit = 0
    for i, obj in enumerate(PyAccountMoveDetail.objects.filter(account_move_id=instance.pk)):
        t_adebit += obj.debit
        t_credit += obj.credit
        obj.company_id = instance.company_id
        obj.save()
        if i == 0:
            instance.company_move = obj.reference_company

    instance.debit = t_adebit
    instance.credit = t_credit
