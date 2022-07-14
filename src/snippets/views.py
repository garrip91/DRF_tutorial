from django.shortcuts import render

from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics


# Create your views here:
class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer