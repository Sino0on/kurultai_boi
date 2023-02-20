from django.urls import path
from .views import *

urlpatterns = [
    path('users/json/', JsonRegisterView.as_view()),
    path('users/list/', UserListView.as_view())
]
