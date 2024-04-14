from django.db import models

from staffs.models import CustomUser


class PaymentCategory(models.Model):
    category = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Payment categories"

    def __str__(self):
        return self.category[:55]


class Payment(models.Model):
    payee = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="payments",
        limit_choices_to={
            "utype": "STU"
        }
    )
    category = models.ForeignKey(
        to=PaymentCategory,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="categories",
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    date_paid = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payee} paid {self.amount} on {self.date_paid.date()}"
