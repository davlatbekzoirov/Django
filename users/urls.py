from .serialazers import SignUpSerialazer
from .views import CreateUserView
from django.urls import path

urlpatterns = [
    path('signup/', CreateUserView.as_view())
]