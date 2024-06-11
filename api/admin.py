from django.contrib import admin

from api.models import BotUser, Product, Order

admin.site.register(BotUser)
admin.site.register(Product)
admin.site.register(Order)
