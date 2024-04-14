from django.urls import path

from .views import *

urlpatterns = [
    path("subjects/", StudentsSubjectsListView.as_view(), name="students_subjects_list"),
    path("payments/", StudentsPaymentsListView.as_view(), name="students_payments_list"),
]