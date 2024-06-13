from .models import BotUser, Product, Order, Operator
from rest_framework.serializers import ModelSerializer


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = [
            'telegram_id',
            'name',
            'phone',
            'latitude',
            'longitude',
            'create_at',
            'language',
        ]


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'product',
            'amount'
        ]


class OperatorSerializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = [
            'text',
            'operator_phone'
        ]
