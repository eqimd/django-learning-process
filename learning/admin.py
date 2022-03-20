from django.contrib import admin

from .models import Student, Course, Lecture

# Register your models here.

admin.site.register([Student, Course, Lecture])
