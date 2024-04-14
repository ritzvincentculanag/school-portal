from django.urls import path

from .views_users import *
from .views_subjects import *

urlpatterns = [
    # Users
    path("users/", CustomUserListView.as_view(), name="users_list"),
    path("users/create/", CustomUserCreateView.as_view(), name="users_create"),
    path("users/update/<int:pk>/", CustomUserUpdateView.as_view(), name="users_update"),
    path("users/delete/<int:pk>/", CustomUserDeleteView.as_view(), name="users_delete"),

    # Subjects
    path("subjects/", SubjectListView.as_view(), name="subjects_list")
]
