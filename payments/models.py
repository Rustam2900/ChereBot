from django.db import models

from utils.models import BaseModel


class PaymentStatus(BaseModel):
    NOT_PAID = 'NOT_PAID'
    PAID = 'PAID'
    PARTIALLY_PAID = 'PARTIALLY_PAID'
    PAYMENT_STATUS_CHOICES = [
        (NOT_PAID, 'Not Paid'),
        (PAID, 'Paid'),
        (PARTIALLY_PAID, 'Partially Paid'),
    ]

    status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=15, default=NOT_PAID)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.get_status_display()
