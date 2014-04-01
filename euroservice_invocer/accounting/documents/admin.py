from django.contrib import admin

from .models import PaymentType, Tax, Invoice, InvoiceRow, InvoicePayment


admin.site.register(PaymentType)
admin.site.register(Tax)
admin.site.register(Invoice)
admin.site.register(InvoiceRow)
admin.site.register(InvoicePayment)
