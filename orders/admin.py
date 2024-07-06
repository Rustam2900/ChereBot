from django.contrib import admin

from orders.models import OrderItem, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'total_amount', 'start_date', 'end_date', 'recurrence')
    search_fields = ('user__phone', 'user__first_name', 'user__last_name', 'address')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    search_fields = ('order__user__phone', 'product__name')
