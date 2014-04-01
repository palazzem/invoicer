from __future__ import unicode_literals
from functools import partial

from django.conf import settings

import moneyed
from djmoney.models.fields import MoneyField as _MoneyField


MoneyField = partial(
    _MoneyField,
    max_digits=30,
    decimal_places=2,
    default=moneyed.Money('0.0', currency=settings.DEFAULT_CURRENCY),
    default_currency=settings.DEFAULT_CURRENCY
)
