from django.urls import path

from staffs.views.users import *
from staffs.views.subjects import *
from staffs.views.semesters import *

urlpatterns = [
    # Users
    path("users/", CustomUserListView.as_view(), name="users_list"),
    path("users/create/", CustomUserCreateView.as_view(), name="users_create"),
    path("users/update/<int:pk>/", CustomUserUpdateView.as_view(), name="users_update"),
    path("users/delete/<int:pk>/", CustomUserDeleteView.as_view(), name="users_delete"),

    # Subjects
    path("subjects/", SubjectListView.as_view(), name="subjects_list"),
    path("subjects/create/", SubjectCreateView.as_view(), name="subjects_create"),
    path("subjects/update/<int:pk>/", SubjectUpdateView.as_view(), name="subjects_update"),
    path("subjects/delete/<int:pk>/", SubjectDeleteView.as_view(), name="subjects_delete"),

    # Semesters
    path("semesters/", SemesterListView.as_view(), name="semesters_list"),
    path("semesters/create/", SemesterCreateView.as_view(), name="semesters_create"),
    path("semesters/update/<int:pk>/", SemesterUpdateView.as_view(), name="semesters_update"),
    path("semesters/delete/<int:pk>/", SemesterDeleteView.as_view(), name="semesters_delete"),
]
