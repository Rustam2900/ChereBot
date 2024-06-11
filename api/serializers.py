from .models import BotUser, UserWater
from rest_framework.serializers import ModelSerializer


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = [
            'user_id',
            'name',
            'username',
            'create_at',
        ]


class UserWaterSerializer(ModelSerializer):
    class Meta:
        model = UserWater
        fields = [
            'title',
            'orders',
            'latitude',
            'longitude',
            'create_at',
        ]
