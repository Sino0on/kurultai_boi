from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from server.models import *
import django_filters.rest_framework


class JsonRegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = Account.objects.filter(is_delegat=True)
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['first_name', 'username']