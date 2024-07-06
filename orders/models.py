from django.db import models
from django.utils import timezone

from products.models import Product
from users.models import User
from utils.models import BaseModel


class Order(BaseModel):
    MONTHLY = 'MONTHLY'
    WEEKLY = 'WEEKLY'

    RECURRENCE_CHOICES = (
        (MONTHLY, 'Monthly'),
        (WEEKLY, 'Weekly'),
    )

    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    ACCEPTED = 'ACCEPTED'
    ACTIVE = 'ACTIVE'
    CANCELLED = 'CANCELLED'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (ACCEPTED, 'Accepted'),
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()  # later change long, lat
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=10)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    recurrence = models.CharField(choices=STATUS_CHOICES, default=MONTHLY, max_length=10)
    next_delivery_date = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} by {self.user.full_name}'


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} {self.price} {self.quantity}'

    @property
    def total_price(self):
        return self.quantity * self.price
