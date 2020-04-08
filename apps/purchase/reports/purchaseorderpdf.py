"""PDF para la purchase order
"""
# Standard Library
import io
import locale

# Django Library
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.purchase.models import PyPurchaseOrder, PyPurchaseOrderDetail
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

locale.setlocale(locale.LC_ALL, '')
locale._override_localeconv = {'mon_thousands_sep': '.'}


def purchase_order_pdf(request, pk):
    """ Función para imprimir la orden de ventas
    """
    response = HttpResponse(content_type='application/pdf')
    pdf_name = _("purchase_order.pdf")
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name

    # Los productos de la orden
    purchase_order = PyPurchaseOrder.objects.get(pk=pk)

    # Los productos de la orden ya en una matriz
    products = PyPurchaseOrderDetail.objects.filter(
        purchase_order_id=pk).only(
        "product_id",
        "description",
        "quantity",
        "price",
        "discount",
        "amount_total"
    )

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Header corporativa
    archivo_imagen = settings.MEDIA_ROOT+'/pyerp-marketing/PyERP_logo_2.png'
    # Definimos el tamaño de la imagen a cargar y las coordenadas
    pdf.drawImage(archivo_imagen, 30, 710, 120, 90, preserveAspectRatio=True)
    pdf.setLineWidth(.3)
    pdf.line(30, 735, 582, 735)

    # Header del reporte
    pdf.setFont('Helvetica', 22)
    pdf.drawString(30, 650, 'Budget # ' + purchase_order.name)

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(30, 625, 'Quotation Date:')

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(180, 625, 'Seller:')

    today = timezone.now()
    pdf.setFont('Helvetica', 12)
    pdf.drawString(30, 610, today.strftime("%Y-%m-%d %H:%M:%S"))

    pdf.setFont('Helvetica', 12)
    pdf.drawString(180, 610, 'Nombre del Vendedor')

    # Alto y ancho de la hoja
    width, height = letter

    # A partir de que altura debriamos imprimir la tabla
    high = 550

    # Header de la tabla
    data_header = []
    data_header.append([
        # "Producto",
        _('Description'),
        _('Quantity'),
        _('Price'),
        _('Discount'),
        _('Subtotal')
    ])

    # Imprimir el header de la tabla
    table = Table(
        data_header,
        colWidths=[7*cm, 3*cm, 3*cm, 3*cm, 3.5*cm]
    )
    table.setStyle(
        TableStyle([
            # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEABOVE', (0, 0), (-1, 0), 1.5, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.black),
            # ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
            ('ALIGN', (1, 0), (-1, 0), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ])
    )
    table.wrapOn(pdf, width, height)
    table.drawOn(pdf, 30, high)

    if products:
        # Cuerpo de la tabla
        data_table = []
        for product in products:
            data_table.append(
                [
                    product.product_id,
                    # product.description,
                    str(product.quantity) + ' Units',
                    product.amount_untaxed,
                    product.discount,
                    locale.format(
                        '%.2f',
                        product.amount_total,
                        grouping=True,
                        monetary=True
                    )
                ]
            )
            high = high - 18

        # Imprimir cuerpo la tabla
        table = Table(
            data_table,
            colWidths=[7*cm, 3*cm, 3*cm, 3*cm, 3.5*cm]
        )
        table.setStyle(
            TableStyle([
                # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                # ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ])
        )

    table.wrapOn(pdf, width, height)
    table.drawOn(pdf, 30, high)

    # Footer de la tabla
    data_foot = []
    data_foot.append(
        ["", _('Net Amount or Affection') + ":", "$ " + locale.format('%.2f', purchase_order.amount_untaxed, grouping=True, monetary=True)]
    )
    data_foot.append(
        ["", _('Exempt Amount') + ":", "$ " + locale.format('%.2f', purchase_order.amount_exempt, grouping=True, monetary=True)]
    )
    data_foot.append(
        ["", _('I.V.A') + ":", "$ " + locale.format('%.2f', purchase_order.amount_tax_iva, grouping=True, monetary=True)]
    )
    data_foot.append(
        ["", _('Other taxes') + ":", "$ " + locale.format('%.2f', purchase_order.amount_tax_other, grouping=True, monetary=True)]
    )
    data_foot.append(
        ["", _('Total taxes') + ":", "$ " + locale.format('%.2f', purchase_order.amount_tax_total, grouping=True, monetary=True)]
    )
    data_foot.append(
        ["", _('Total') + ":", "$ " + locale.format('%.2f', purchase_order.amount_total, grouping=True, monetary=True)]
    )

    high = high - (18 * 7)
    # Imprimir cuerpo la tabla
    table = Table(
        data_foot,
        colWidths=[11*cm, 5*cm, 3.5*cm]
    )
    table.setStyle(
        TableStyle([
            # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            # ('LINEBELOW', (1, 0), (2, 0), 1.5, colors.black),
            # ('LINEBELOW', (1, 0), (2, 2), 0.5, colors.black),
            ('LINEBELOW', (1, 3), (2, 3), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            # ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (1, 0), (1, 5), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTNAME', (1, 2), (1, 2), 'Helvetica-Bold'),
        ])
    )
    table.wrapOn(pdf, width, height)
    table.drawOn(pdf, 30, high)

    # Close the PDF object cleanly, and we're done.
    pdf.showPage()
    pdf.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    response.write(buffer.getvalue())

    return response
