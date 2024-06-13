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


class OperatorApiView(ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
