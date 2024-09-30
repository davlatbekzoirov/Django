from django.urls import path
from .views import meeting_list, meeting_room, create_meeting

urlpatterns = [
    path('meetings/', meeting_list, name='meeting_list'),  
    path('meeting/<str:room_name>/', meeting_room, name='meeting_room'),
    path('create/', create_meeting, name='create_meeting'),    
]
