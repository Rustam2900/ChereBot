from django.urls import path
from .views import BotUserApiView, UserWaterApiView

urlpatterns = [
    path('botusers/', BotUserApiView.as_view()),
    path('userwater/', UserWaterApiView.as_view())

]
