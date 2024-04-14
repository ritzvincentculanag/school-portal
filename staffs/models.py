from django.db import models
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True, null=False, blank=False)
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    units = models.SmallIntegerField(null=False, blank=False)
    lec_hours = models.SmallIntegerField(null=False, blank=False)
    lab_hours = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.title[:55]}"


class CustomUser(AbstractUser):
    UTYPE_STU = "STU"
    UTYPE_TEA = "TEA"
    UTYPE_CAS = "CAS"
    UTYPE_STA = "STA"

    UTYPES = (
        (UTYPE_STU, "Student"),
        (UTYPE_TEA, "Teacher"),
        (UTYPE_CAS, "Cashier"),
        (UTYPE_STA, "Staff")
    )

    subjects = models.ManyToManyField(to=Subject, related_name="subjects")
    utype = models.CharField(
        max_length=20,
        choices=UTYPES,
        default=UTYPE_STA,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AcademicYear(models.Model):
    start_year = models.IntegerField(unique=True, null=False, blank=False)
    end_year = models.IntegerField(unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.start_year}-{self.end_year}"


class Semester(models.Model):
    SEM_1 = '1ST'
    SEM_2 = '2ND'
    SEM_3 = '3RD'
    SEM_4 = 'SUM'

    SEMS = (
        (SEM_1, 'First Semester'),
        (SEM_2, 'Second Semester'),
        (SEM_3, 'Third Semester'),
        (SEM_4, 'Summer')
    )

    semester = models.CharField(max_length=20, choices=SEMS, null=False, blank=False, unique=True)
    academic_year = models.ForeignKey(
        to=AcademicYear,
        related_name="academic_year",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    class Meta:
        unique_together = ("semester", "academic_year")

    def __str__(self):
        return f"{self.semester} Semester of {self.academic_year}"


class Advertisement(models.Model):
    banner = models.ImageField(upload_to="advertisement_banners/", blank=True, null=True)
    title = models.CharField(max_length=512, null=False, blank=False)
    author = models.ForeignKey(to=CustomUser, related_name="author", on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
