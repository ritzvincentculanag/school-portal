from django.urls import path

from .views_users import *

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="users_list"),
]