from django.contrib import admin
from .models import AddCollege, AddTeacher, AddSchool

# Register your models here.
admin.site.register(AddSchool)
admin.site.register(AddCollege)
admin.site.register(AddTeacher)
