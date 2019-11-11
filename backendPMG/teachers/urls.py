from django.urls import path
from . import views

urlpatterns = [
    path('', views.teachersList, name='teachersList'),
    path('praise/<int: teacher_id>', views.praiseTeacher, name='praiseTeacher'),
    path('teacher/<int: teacher_id>', views.teacher, name='teacher')
]
