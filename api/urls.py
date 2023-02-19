from django.urls import path
from .views import *

urlpatterns = [
    path('users/json/', JsonRegisterView.as_view())
]
