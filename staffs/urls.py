from django.urls import path

from .views_users import *

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="users_list"),
    path("users/create/", CustomUserCreateView.as_view(), name="users_create"),
    path("users/update/<int:pk>/", CustomUserUpdateView.as_view(), name="users_update"),
    path("users/delete/<int:pk>/", CustomUserDeleteView.as_view(), name="users_delete"),
]
