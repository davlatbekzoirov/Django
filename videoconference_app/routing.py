from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/webinar/(?P<meeting_id>[a-zA-Z0-9-]+)/$', consumers.WebinarConsumer.as_asgi()),
]
