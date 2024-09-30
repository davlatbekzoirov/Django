from django.urls import path
from .views import meeting_room, create_meeting

urlpatterns = [
    path('meeting/<str:room_name>/', meeting_room, name='meeting_room'),
    path('create/', create_meeting, name='create_meeting'),  # Yangi URL qo'shildi
]
