from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.schedule_view, name='index'),
    path("dashboard/", views.schedule_dashboard, name='dashboard')
]
