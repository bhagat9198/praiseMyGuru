from django.urls import path
from . import views

urlpatterns = [
    path('', views.schoolsList, name='schoolsList'),
    path('<int: school_id>', views.school, name='school')
]
