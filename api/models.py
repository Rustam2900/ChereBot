from django.db import models


class LanguageCodes(models.TextChoices):
    EN = 'en', 'English'
    UZ = 'uz', 'Uzbek'
    RU = 'ru', 'Russian'


class BotUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    create_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        max_length=2,
        choices=LanguageCodes.choices,
        default=LanguageCodes.UZ
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.description


class Order(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='order')
    product = models.BigIntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.amount
