from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import *

from staffs.forms import CustomUserCreationForm
from staffs.models import CustomUser


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = "users"
    template_name = "staffs/users/users_list.html"

    def get_queryset(self):
        query = self.request.GET.get("users_search")
        utype = self.request.GET.get("utype")
        users = CustomUser.objects.all()

        if utype:
            users = users.filter(utype=utype)
        if query:
            users = users.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )

        return users


class CustomUserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users_list")
    template_name = "staffs/users/users_create.html"
