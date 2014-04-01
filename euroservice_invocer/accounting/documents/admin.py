from django.contrib import admin

from .models import PaymentType, Tax, Invoice, InvoiceRow, InvoicePayment, CreditNote, CreditNoteRow


admin.site.register(PaymentType)
admin.site.register(Tax)
admin.site.register(Invoice)
admin.site.register(InvoiceRow)
admin.site.register(InvoicePayment)
admin.site.register(CreditNote)
admin.site.register(CreditNoteRow)
