from django.urls import path

from .views.payments import *

urlpatterns = [
    # Payments
    path('payments/', PaymentListView.as_view(), name='payments_list'),
    path('payments/create/', PaymentCreateView.as_view(), name='payments_create'),
    path('payments/<int:pk>/update/', PaymentUpdateView.as_view(), name='payments_update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payments_delete'),
]
