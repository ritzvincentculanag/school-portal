from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.urls import reverse_lazy

from staffs.models import Advertisement
from staffs.mixins import StaffRequiredMixin


class AdvertisementListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Advertisement
    template_name = 'staffs/advertisements/advertisement_list.html'
    context_object_name = 'advertisements'


class AdvertisementCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Advertisement
    fields = '__all__'
    template_name = 'staffs/advertisements/advertisement_create.html'
    success_url = reverse_lazy('advertisements_list')


class AdvertisementUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Advertisement
    fields = '__all__'
    template_name = 'staffs/advertisements/advertisement_update.html'
    success_url = reverse_lazy('advertisements_list')
    context_object_name = 'advertisement'


class AdvertisementDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Advertisement
    template_name = "staffs/advertisements/advertisement_delete.html"
    success_url = reverse_lazy('advertisements_list')
    context_object_name = 'advertisement'


class AdvertisementDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    model = Advertisement
    fields = '__all__'
    template_name = 'staffs/advertisements/advertisement_detail.html'
    context_object_name = 'advertisement'
