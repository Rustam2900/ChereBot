from django.urls import path
from api.views import (BotUserApiView, ProductApiView,
                       OrderUserApiView, OrderCompanyApiView, OperatorApiView, BotCompanyApiView)

urlpatterns = [
    path('botcompany/<int:telegram_id>/', BotCompanyApiView.as_view()),
    path('botuser/<int:telegram_id>/', BotUserApiView.as_view()),
    path('product/', ProductApiView.as_view()),
    path('order-company/', OrderCompanyApiView.as_view()),
    path('order-user/', OrderUserApiView.as_view()),
    path('operator/', OperatorApiView.as_view()),
]
