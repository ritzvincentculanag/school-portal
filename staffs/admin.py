from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(AcademicYear)
admin.site.register(Semester)
admin.site.register(Advertisement)
