from django.urls import path

from .views import *

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="users_list"),
]