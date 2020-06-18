# chat/routing.py
from django.conf.urls import url
from . import guest

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', guest.ChatConsumer),
    #URL 파라미터에서 room_name 획득
]