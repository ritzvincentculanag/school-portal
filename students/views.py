import decimal
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from cashiers.models import Payment, Tuition


class StudentsSubjectsListView(LoginRequiredMixin, TemplateView):
    template_name = 'students/subjects_list.html'


class StudentsPaymentsListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'students/payments_list.html'
    context_object_name = 'payments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payments = self.get_queryset()
        tuitions = Tuition.objects.filter(user=self.request.user).first()
        remaining_balance = tuitions.amount if tuitions else 0.00
        total_paid: decimal.Decimal = decimal.Decimal('0.00')

        for payment in payments:
            total_paid = total_paid + payment.amount

        context['payments'] = payments
        context['total_paid'] = total_paid
        context['remaining_balance'] = remaining_balance
        return context

    def get_queryset(self):
        payments = Payment.objects.filter(payee=self.request.user)

        if not payments.exists():
            return payments.none()

        return payments
