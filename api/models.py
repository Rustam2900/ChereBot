from django.db import models


class BotCompany(models.Model):
    # LANGUAGE_CHOICES = [
    #     ('uz', 'O\'zbekcha'),
    #     ('ru', 'Русский'),
    # ]

    telegram_id = models.BigIntegerField(unique=True)
    # language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    company_name = models.CharField(max_length=100)
    employee_number = models.IntegerField()
    lifetime = models.IntegerField()
    company_employee_name = models.CharField(max_length=100)
    company_contact = models.CharField(max_length=35)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class BotUser(models.Model):
    # LANGUAGE_CHOICES = [
    #     ('uz', 'O\'zbekcha'),
    #     ('ru', 'Русский'),
    # ]

    telegram_id = models.BigIntegerField(unique=True)
    # language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=35)
    add_contact = models.CharField(max_length=35)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.description


class OrderCompany(models.Model):
    bot_company_id = models.ForeignKey(BotCompany, on_delete=models.CASCADE, related_name='order_company')
    create_at = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    def __str__(self):
        return self.product_name


class OrderUser(models.Model):
    bot_user_id = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='order_user')
    create_at = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    def __str__(self):
        return self.product_name


class Operator(models.Model):
    text = models.TextField()
    operator_phone = models.CharField(max_length=30)

    def __str__(self):
        return self.text
