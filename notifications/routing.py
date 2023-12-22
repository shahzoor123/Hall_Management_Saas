# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
      re_path(r'ws/stock/notifications/$', consumers.StockNotificationConsumer.as_asgi()),
]