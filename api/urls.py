from django.urls import path
from .views import BotUserApiView, ProductApiView, OrderApiView

urlpatterns = [
    path('botusers/', BotUserApiView.as_view()),
    path('product/', ProductApiView.as_view()),
    path('order/', OrderApiView.as_view())
]
