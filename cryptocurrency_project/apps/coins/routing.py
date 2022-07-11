from django.urls import path

from .consumers import CoinsListConsumer

websocket_urlpatterns = [
    path('ws/coins/', CoinsListConsumer.as_asgi())
]