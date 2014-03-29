from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models


@python_2_unicode_compatible
class Partner(models.Model):
    """
    Customer or supplier registry
    """
    name = models.CharField(_('Name'), max_length=100)
    vat_number = models.CharField(_('VAT number'), max_length=16, null=True, blank=True)
    social_number = models.CharField(_('Social number'), max_length=16, null=True, blank=True)
    address = models.CharField(_('Address'), max_length=200)
    city = models.CharField(_('City'), max_length=100)
    province = models.CharField(_('Province'), max_length=2)
    zip = models.PositiveSmallIntegerField(_('Zip'), max_length=5)

    website = models.URLField(_('Website'), null=True, blank=True)
    # TODO: add default payment option

    customer = models.BooleanField(_('Customer'), default=True)
    supplier = models.BooleanField(_('Supplier'), default=False)
    notes = models.TextField(_('Notes'), blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Contact(models.Model):
    """
    Employee or manager information
    """
    firstname = models.CharField(_('First name'), max_length=100)
    lastname = models.CharField(_('Last name'), max_length=100)
    job_position = models.CharField(_('Job position'), max_length=100, null=True, blank=True)
    notes = models.TextField(_('Notes'), blank=True, null=True)
    partner = models.ForeignKey(Partner)

    def __str__(self):
        return '{0} {1}'.format(self.firstname, self.lastname)


@python_2_unicode_compatible
class Reference(models.Model):
    TYPE_CHOICE = (
        (0, _('Email')),
        (1, _('Phone')),
        (2, _('Fax')),
        (3, _('Mobile')),
    )

    type = models.PositiveSmallIntegerField(_('Reference type'), choices=TYPE_CHOICE)
    value = models.CharField(_('Value'), max_length=50)

    def __str__(self):
        return '{0}: {1}'.format(self.type, self.value)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class PartnerReference(Reference):
    """
    Reference contacts for employees or companies
    """
    partner = models.ForeignKey(Partner)

    def __str__(self):
        return '{0} {1}: {2}'.format(self.partner, self.get_type_display(), self.value)


@python_2_unicode_compatible
class ContactReference(Reference):
    """
    Reference contacts for employees or companies
    """
    contact = models.ForeignKey(Contact)

    def __str__(self):
        return '{0} {1}: {2}'.format(self.partner, self.get_type_display(), self.value)
