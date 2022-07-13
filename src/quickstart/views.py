from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framewok import viewsets

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


# Create your views here:
class UserViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, которая позволяет пользователям просматривать или редактировать
    """