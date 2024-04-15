from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from cashiers.models import Payment, Tuition
from staffs.mixins import CashierRequiredMixin
from staffs.models import Semester


class PaymentListView(LoginRequiredMixin, CashierRequiredMixin, ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'cashiers/payments/payments_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['semesters'] = Semester.objects.all()
        return context

    def get_queryset(self):
        semester = self.request.GET.get('semester')
        payments = Payment.objects.all()

        if semester:
            payments = payments.filter(semester=semester)

        return payments


class PaymentCreateView(LoginRequiredMixin, CashierRequiredMixin, CreateView):
    model = Payment
    fields = '__all__'
    success_url = reverse_lazy('payments_list')
    template_name = 'cashiers/payments/payments_create.html'

    def form_valid(self, form):
        user = form.instance.payee
        user_tuition = Tuition.objects.filter(user=user).first()
        payment_amount = form.instance.amount

        print(user)
        print(user_tuition)

        # Check if payment exceeds tuition amount
        if payment_amount > user_tuition.amount:
            user_tuition.amount = 0.00
            user_tuition.save()

            return super().form_valid(form)

        # Subtract tuition from payment
        user_tuition.amount = user_tuition.amount - payment_amount
        user_tuition.save()

        return super().form_valid(form)


class PaymentUpdateView(LoginRequiredMixin, CashierRequiredMixin, UpdateView):
    model = Payment
    fields = '__all__'
    context_object_name = 'payment'
    success_url = reverse_lazy('payments_list')
    template_name = 'cashiers/payments/payments_update.html'

    def form_valid(self, form):
        user = form.instance.user
        user_tuition = Tuition.objects.filter(user=user).first()
        payment_before = Payment.objects.filter(pk=self.kwargs.get('pk')).first()
        payment_amount = form.instance.amount

        # Add back payment amount
        user_tuition.amount = user_tuition.amount + payment_before.amount
        user_tuition.save()

        # Check if payment exceeds tuition amount
        if payment_amount > user_tuition.amount:
            user_tuition.amount = 0.00
            user_tuition.save()

            return super().form_valid(form)

        # Subtract tuition from payment
        user_tuition.amount = user_tuition.amount - payment_amount
        user_tuition.save()

        return super().form_valid(form)


class PaymentDeleteView(LoginRequiredMixin, CashierRequiredMixin, DeleteView):
    model = Payment
    context_object_name = 'payment'
    success_url = reverse_lazy('payments_list')
    template_name = 'cashiers/payments/payments_delete.html'

    def form_valid(self, form):
        payment_before = Payment.objects.filter(pk=self.kwargs.get('pk')).first()
        user = payment_before.payee
        user_tuition = Tuition.objects.filter(user=user).first()
        user_tuition.amount = user_tuition.amount + payment_before.amount
        user_tuition.save()

        return super().form_valid(form)
