from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class JsonRegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
