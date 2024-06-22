from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import BotUser, Product, Order, Operator
from .serializers import BotUserSerializers, ProductSerializers, OrderSerializer, OperatorSerializer
from rest_framework.generics import ListCreateAPIView


class BotUserApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class OrderApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id', None)
        if telegram_id is not None:
            return Order.objects.filter(user_id__telegram_id=telegram_id)
        return Order.objects.all()

    def create(self, request, *args, **kwargs):
        telegram_id = request.data.get('telegram_id')
        if not telegram_id:
            raise ValidationError({'telegram_id': 'This field is required.'})

        try:
            user = BotUser.objects.get(telegram_id=telegram_id)
        except BotUser.DoesNotExist:
            raise ValidationError({'telegram_id': 'User with this telegram_id does not exist.'})

        # Replace 'user_id' with the actual user instance
        request.data['user_id'] = user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OperatorApiView(ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
