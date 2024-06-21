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
    serializer_class = OrderSerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id', None)
        if telegram_id is not None:
            return Order.objects.filter(user_id__telegram_id=telegram_id)
        return Order.objects.all()


class OperatorApiView(ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
