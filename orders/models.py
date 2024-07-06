from django.db import models
from django.utils import timezone

from products.models import Product
from users.models import User
from utils.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()  # later change long, lat
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    recurrence = models.CharField(max_length=50, null=True, blank=True)
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
