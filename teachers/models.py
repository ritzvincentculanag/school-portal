from django.db import models

from staffs.models import CustomUser, Subject, Semester


class SubjectGrade(models.Model):
    prelim = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    midterm = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    prefinal = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    final = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    semester = models.ForeignKey(
        to=Semester,
        related_name="sem",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    student = models.ForeignKey(
        to=CustomUser,
        related_name="student",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        limit_choices_to={
            "utype": "STU",
        }
    )
    subject = models.ForeignKey(
        to=Subject,
        related_name="grades",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    class Meta:
        unique_together = ("student", "subject")

    def __str__(self):
        return f"{self.student}'s grades"


class SubjectTeacher(models.Model):
    subject = models.ForeignKey(
        to=Subject,
        related_name="teachers",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    teacher = models.ForeignKey(
        to=CustomUser,
        related_name="teacher",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        limit_choices_to={
            "utype": "TEA",
        }
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("subject", "teacher")

    def __str__(self):
        return f"{self.subject} | {self.teacher}"
