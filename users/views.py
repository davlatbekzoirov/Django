from django.shortcuts import render
from .serialazers import SignUpSerialazer
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions

# Create your views here.
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = SignUpSerialazer