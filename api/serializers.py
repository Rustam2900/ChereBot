from .models import BotUser, UserWater
from rest_framework.serializers import ModelSerializer


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'


class UserWaterSerializer(ModelSerializer):
    class Meta:
        model = UserWater
        fields = '__all__'
