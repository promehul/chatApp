# chat/routing.py
from django.conf.urls import url

from . import consumers

fuck khetu_bb
websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
