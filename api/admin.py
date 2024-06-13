from django.contrib import admin

from api.models import BotUser, Product, Order, Operator

admin.site.register(BotUser)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Operator)
