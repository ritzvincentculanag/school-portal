from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

from staffs.models import CustomUser


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = "user"
    template_name = "staffs/users/users_list.html"
