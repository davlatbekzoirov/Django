from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('single/', views.single, name='single'),
    path('teacher/', views.teacher, name='teacher'),
    path('base/', views.base, name='base'),
]
