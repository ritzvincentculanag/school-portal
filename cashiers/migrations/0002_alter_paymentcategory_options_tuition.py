# Generated by Django 4.2 on 2024-04-14 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("staffs", "0008_advertisement_content_and_more"),
        ("cashiers", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paymentcategory",
            options={"verbose_name_plural": "Payment categories"},
        ),
        migrations.CreateModel(
            name="Tuition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=9)),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staffs.semester",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        limit_choices_to={"utype": "STU"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
