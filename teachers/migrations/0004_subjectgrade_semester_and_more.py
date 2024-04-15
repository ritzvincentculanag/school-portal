# Generated by Django 4.2 on 2024-04-14 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("staffs", "0009_alter_customuser_utype"),
        ("teachers", "0003_alter_subjectgrade_subject_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subjectgrade",
            name="semester",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sem",
                to="staffs.semester",
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="subjectgrade",
            unique_together={("student", "subject")},
        ),
        migrations.AlterUniqueTogether(
            name="subjectteacher",
            unique_together={("subject", "teacher")},
        ),
    ]
