from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from server.models import *


class JsonRegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = Account.objects.filter(is_delegat=True)