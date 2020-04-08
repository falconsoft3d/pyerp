# Django Library
from django.contrib import admin

# Thirdparty Library
from apps.purchase.models import PyPurchaseOrder, PyPurchaseOrderDetail

# Register your models here.


class PyPurchaseOrderDetailInline(admin.TabularInline):
    model = PyPurchaseOrderDetail
    extra = 1
    fields = [
        # 'purchase_order_id',
        'product',
        'description',
        'quantity',
        # 'measure_unit',
        # 'product_tax',
        'amount_untaxed',
        'discount',
        # 'amount_total',
    ]


class PyPurchaseOrderAdmin(admin.ModelAdmin):
    fields = ['partner_id']
    inlines = [PyPurchaseOrderDetailInline]


admin.site.register(PyPurchaseOrder, PyPurchaseOrderAdmin)
