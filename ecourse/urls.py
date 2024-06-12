from django.urls import path
from . import views

urlpatterns = [
    path('ecourse/', views.Ecourse, name='ecourse'),
]
