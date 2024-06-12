from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage),
    path('job/<int:pk>', views.Job.as_view(), name='job'),
    path('not_access/', views.not_access),
    path('add_jobs/', views.add_jobs),
    path('message_about/', views.message_about, name='message_about')
]