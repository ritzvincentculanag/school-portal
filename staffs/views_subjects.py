from django.contrib.auth.mixins import LoginRequiredMixin
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
