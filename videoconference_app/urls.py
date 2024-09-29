# webinars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.webinar_list, name='meeting_list'),
    path('create/', views.create_meeting, name='create_meeting'),
    path('meeting/<str:meeting_id>/', views.meeting_detail, name='meeting_detail'),
]
