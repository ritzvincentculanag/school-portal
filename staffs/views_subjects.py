from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from staffs.models import Subject

from .mixins import StaffRequiredMixin


class SubjectListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'staffs/subjects/subjects_list.html'

    def get_queryset(self):
        query = self.request.GET.get('subjects_search')
        if query is None:
            return Subject.objects.all()

        return Subject.objects.filter(title__icontains=query)


class SubjectCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Subject
    fields = '__all__'
    template_name = 'staffs/subjects/subjects_create.html'
    success_url = reverse_lazy('subjects_list')


class SubjectUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Subject
    fields = '__all__'
    context_object_name = 'subject'
    template_name = 'staffs/subjects/subjects_update.html'
    success_url = reverse_lazy('subjects_list')


class SubjectDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Subject
    context_object_name = 'subject'
    success_url = reverse_lazy('subjects_list')
    template_name = 'staffs/subjects/subjects_delete.html'
