from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from staffs.models import Advertisement


# Create your views here.
class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('users_list')
            else:
                return redirect('students_subjects_list')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            super().form_valid(form)

            if form.get_user().is_staff:
                return redirect('users_list')
            else:
                return redirect('students_subjects_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisements = Advertisement.objects.all()
        context.update(advertisements=advertisements)

        return context
