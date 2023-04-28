from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from rest_framework import permissions
from .models import Post
from .permissions import IsAuthororReadOnly

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthororReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthororReadOnly, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
