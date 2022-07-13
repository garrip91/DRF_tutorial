from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framewok import viewsets

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


# Create your views here:
class UserViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, которая позволяет пользователям просматривать или редактировать
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, которая позволяет просматривать или редактировать группы
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer