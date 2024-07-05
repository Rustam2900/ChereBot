from django.contrib import admin

from api.models import BotUser, Product, OrderUser, OrderCompany, Operator, BotCompany

admin.site.register(BotUser)
admin.site.register(Product)
admin.site.register(OrderUser)
admin.site.register(OrderCompany)
admin.site.register(Operator)
admin.site.register(BotCompany)
