from django.db import models


class BotUser(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserWater(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    orders = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

