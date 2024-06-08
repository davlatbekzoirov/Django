from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("schedule/", views.schedule_view, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/lab_data/<str:lab_id>/', views.get_lab_data, name='get_lab_data'),
]