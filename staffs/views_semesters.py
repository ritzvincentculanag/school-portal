from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from staffs.models import Semester

from .mixins import StaffRequiredMixin


class SemesterListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Semester
    context_object_name = 'semesters'
    template_name = 'staffs/semesters/semesters_list.html'


class SemesterCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Semester
    fields = '__all__'
    template_name = 'staffs/semesters/semesters_create.html'
    success_url = reverse_lazy('semesters_list')


class SemesterUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Semester
    fields = '__all__'
    context_object_name = 'semester'
    template_name = 'staffs/semesters/semesters_update.html'
    success_url = reverse_lazy('semesters_list')


class SemesterDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Semester
    context_object_name = 'semester'
    success_url = reverse_lazy('semesters_list')
    template_name = 'staffs/semesters/semesters_delete.html'
