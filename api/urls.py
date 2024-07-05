from django.urls import path
from api.views import (BotUserApiView, ProductApiView,
                       OrderUserApiView, OrderCompanyApiView, OperatorApiView, BotCompanyApiView)

urlpatterns = [
    path('botcompany/', BotCompanyApiView.as_view()),
    path('botusers/', BotUserApiView.as_view()),
    path('product/', ProductApiView.as_view()),
    path('order-company/', OrderCompanyApiView.as_view()),
    path('order-user/', OrderUserApiView.as_view()),
    path('operator/', OperatorApiView.as_view()),
]
