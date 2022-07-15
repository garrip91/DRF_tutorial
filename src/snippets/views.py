from django.shortcuts import render

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, generics, permissions, viewsets
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


# Create your views here:
# class SnippetList(generics.ListCreateAPIView):

    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer

    # def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)

    # permission_classes = (IsOwnerOrReadOnly,)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer

    # # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class SnippetHighlight(generics.GenericAPIView):

    # queryset = Snippet.objects.all()
    # renderer_classes = [renderers.StaticHTMLRenderer]

    # def get(self, request, *args, **kwargs):
        # snippet = self.get_object()
        # return Response(snippet.highlighted)


class SnippetViewSet(viewsets.ModelViewSet):
    """
    Этот набор представлений автоматически обеспечивает работу таких методов как `list`, `create`, `retrieve`,
    `update` and `destroy`.
    Кроме того, здесь предоставляется дополнительное действие `highlight`
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class UserList(generics.ListAPIView):

    # queryset = User.objects.all()
    # serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):

    # queryset = User.objects.all()
    # serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Этот набор представлений автоматически создает действия `list` и `detail`
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer