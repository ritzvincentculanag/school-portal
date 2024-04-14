from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.utype == "STA"

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('login'))


class TeacherRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.utype == "TEA"

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('login'))


class CashierRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.utype == "CAS"

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('login'))
