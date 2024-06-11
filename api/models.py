from django.db import models


class LanguageCodes(models.TextChoices):
    EN = 'en', 'English'
    UZ = 'uz', 'Uzbek'
    RU = 'ru', 'Russian'


class BotUser(models.Model):
    telegram_id = models.BigIntegerField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
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
    pass
