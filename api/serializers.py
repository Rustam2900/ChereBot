from .models import BotCompany, Product, OrderUser, Operator, BotUser, OrderCompany
from rest_framework.serializers import ModelSerializer


class BotCompanySerializers(ModelSerializer):
    class Meta:
        model = BotCompany
        fields = [
            'telegram_id',
            'language',
            'company_name',
            'employee_number',
            'lifetime',
            'company_employee_name',
            'company_contact',
            'create_at'

        ]


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'

        ]


class OrderCompanySerializer(ModelSerializer):
    class Meta:
        model = OrderCompany
        fields = [
            'bot_company_id',
            'create_at',
            'product_name',
            'amount',
            'latitude',
            'longitude'
        ]


class OrderUserSerializer(ModelSerializer):
    class Meta:
        model = OrderUser
        fields = [
            'bot_user_id',
            'create_at',
            'product_name',
            'amount',
            'latitude',
            'longitude'
        ]


class OperatorSerializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = [
            'text',
            'operator_phone'
        ]


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = [
            'telegram_id',
            'language',
            'name',
            'contact',
            'add_contact',
            'create_at'

        ]
