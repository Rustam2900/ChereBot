from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from api.models import BotCompany, Product, OrderCompany, OrderUser, Operator, BotUser
from api.serializers import BotUserSerializers, ProductSerializers, OrderUserSerializer, OrderCompanySerializer, \
    OperatorSerializer, \
    BotCompanySerializers
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class BotCompanyApiView(RetrieveAPIView):
    queryset = BotCompany.objects.all()
    serializer_class = BotCompanySerializers
    lookup_field = 'telegram_id'


class BotUserApiView(RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers
    lookup_field = 'telegram_id'


class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class OrderCompanyApiView(ListCreateAPIView):
    queryset = OrderUser.objects.all()
    serializer_class = OrderCompanySerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id', None)
        if telegram_id is not None:
            return OrderCompany.objects.filter(bot_company_id__telegram_id=telegram_id)
        return OrderCompany.objects.all()

    def create(self, request, *args, **kwargs):
        telegram_id = request.data.get('telegram_id')
        if not telegram_id:
            raise ValidationError({'telegram_id': 'This field is required.'})

        try:
            user = BotCompany.objects.get(telegram_id=telegram_id)
        except BotCompany.DoesNotExist:
            raise ValidationError({'telegram_id': 'User with this telegram_id does not exist.'})

        # Replace 'user_id' with the actual user instance
        request.data['bot_company_id'] = user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderUserApiView(ListCreateAPIView):
    queryset = OrderUser.objects.all()
    serializer_class = OrderUserSerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id', None)
        if telegram_id is not None:
            return OrderUser.objects.filter(bot_user_id__telegram_id=telegram_id)
        return OrderUser.objects.all()

    def create(self, request, *args, **kwargs):
        telegram_id = request.data.get('telegram_id')
        if not telegram_id:
            raise ValidationError({'telegram_id': 'This field is required.'})

        try:
            user = BotUser.objects.get(telegram_id=telegram_id)
        except BotUser.DoesNotExist:
            raise ValidationError({'telegram_id': 'User with this telegram_id does not exist.'})

        # Replace 'user_id' with the actual user instance
        request.data['bot_user_id'] = user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OperatorApiView(ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
