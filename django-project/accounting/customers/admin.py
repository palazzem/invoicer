from django.contrib import admin

from .models import Partner, Contact, ContactReference, PartnerReference


admin.site.register(Partner)
admin.site.register(PartnerReference)
admin.site.register(Contact)
admin.site.register(ContactReference)
