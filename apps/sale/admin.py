# Django Library
from django.contrib import admin

# Thirdparty Library
from apps.sale.models import PySaleOrder, PySaleOrderDetail, PySaleOrderState

# Register your models here.


class PySaleOrderDetailInline(admin.TabularInline):
    model = PySaleOrderDetail
    extra = 1
    fields = [
            # 'sale_order_id',
            'product',
            'description',
            'quantity',
            # 'measure_unit',
            # 'product_tax',
            'amount_untaxed',
            'discount',
            # 'amount_total',
        ]


class PySaleOrderAdmin(admin.ModelAdmin):
    fields = ['partner_id']
    inlines = [PySaleOrderDetailInline]


admin.site.register(PySaleOrder, PySaleOrderAdmin)

admin.site.register(PySaleOrderState)