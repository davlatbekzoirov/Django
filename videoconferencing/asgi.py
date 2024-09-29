# your_project/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from videoconference_app import consumers  # WebRTC signaling uchun consumer'ni qo'shish

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoconferencing.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/webinar/<str:meeting_id>/", consumers.WebRTCConsumer.as_asgi()),
            ]
        )
    ),
})
