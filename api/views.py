from .models import BotUser, UserWater
from .serializers import BotUserSerializers, UserWaterSerializer
from rest_framework.generics import ListCreateAPIView


class BotUserApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class UserWaterApiView(ListCreateAPIView):
    queryset = UserWater.objects.all()
    serializer_class = UserWaterSerializer
