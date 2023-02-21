from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from server.models import *
from django_filters import rest_framework as filters
from server.filters import UserFilterForm
from rest_framework.permissions import IsAdminUser


class JsonRegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = Account.objects.filter(is_delegat=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilterForm
    permission_classes = (IsAdminUser, )
