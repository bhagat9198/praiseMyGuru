from django.urls import path
from . import views

urlpatterns = [
    path('', views.collegesList, name='collegesList'),
    path('<int: college_id>', views.college, name='college')
]
