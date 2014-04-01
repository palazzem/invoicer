from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models

from ..customers.models import Partner
from .fields import MoneyField


@python_2_unicode_compatible
class PaymentType(models.Model):
    """
    Invoice payment type
    """
    name = models.CharField(_('Payment name'), max_length=50)
    description = models.CharField(_('Description'), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tax(models.Model):
    """
    Defines many taxes applicable to Invoice.
    "Taxable" field means this tax could be taxed another time
    """
    name = models.CharField(_('Tax name'), max_length=50)
    amount = models.DecimalField(_('Amount (%)'), max_digits=5, decimal_places=2)
    taxable = models.BooleanField(_('Taxable'), default=False)

    def __str__(self):
        return self.name


class Document(models.Model):
    """
    Generic document model
    If "Number" is null then this invoice is a "proforma"
    """
    STATUS_CHOICE = (
        (0, _('Draft')),
        (1, _('Sent')),
        (3, _('Paid')),
    )

    status = models.PositiveSmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=0)
    number = models.PositiveIntegerField(_('Number'), unique_for_year='date', null=True, blank=True)
    date = models.DateField(_('Emission date'))
    customer = models.ForeignKey(Partner, verbose_name=_('Customer'))

    def validate_unique(self, *args, **kwargs):
        if self.number:
            super(Document, self).validate_unique(*args, **kwargs)

    class Meta:
        abstract = True


class DocumentRow(models.Model):
    description = models.CharField(_('Description'), max_length=200)
    quantity = models.PositiveIntegerField(_('Quantity'))
    amount = MoneyField(_('Amount'))
    tax = models.ForeignKey(Tax, verbose_name=_('Tax'), blank=True, null=True)

    @property
    def value(self):
        return self.quantity * self.amount

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Invoice(Document):
    payment_type = models.ForeignKey(PaymentType, verbose_name=_('Payment type'))
    taxes = models.ManyToManyField(Tax, blank=True, null=True, verbose_name=_('Taxes'))

    def __str__(self):
        if self.number:
            prefix = _('Invoice n.')
        else:
            prefix = _('Proforma n.')

        return '{0} {1}/{2}'.format(prefix, self.number, str(self.date.year)[-2:])


@python_2_unicode_compatible
class InvoiceRow(DocumentRow):
    """
    Single invoice element.
    "Taxable" means if this item should be taxed or not
    """
    taxable = models.BooleanField(_('Taxable'), default=True)
    invoice = models.ForeignKey(Invoice, verbose_name=_('Invoice'))

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class InvoicePayment(models.Model):
    """
    Invoice payments
    """
    date = models.DateField(_('Payment date'))
    amount = MoneyField(_('Amount'))
    invoice = models.ForeignKey(Invoice, verbose_name=_('Invoice'))

    def __str__(self):
        return '{0} {1} {2}'.format(_('Invoice n.'), _('paid'), self.date)


@python_2_unicode_compatible
class CreditNote(Document):

    def __str__(self):
        return '{0} {1}/{2}'.format(_('Credit note n.'), self.number, str(self.date.year)[-2:])


@python_2_unicode_compatible
class CreditNoteRow(DocumentRow):
    credit_note = models.ForeignKey(CreditNote, verbose_name=_('Credit note'))

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class ExpenseNote(models.Model):
    description = models.CharField(_('Description'), max_length=200)
    date = models.DateField(_('Date'))
    amount = MoneyField(_('Amount'))
    consumed = models.BooleanField(_('Consumed'), default=False)
    customer = models.ForeignKey(Partner, verbose_name=_('Customer'))

    def __str__(self):
        return self.description
