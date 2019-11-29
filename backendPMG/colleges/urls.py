from django.urls import path
from . import views

urlpatterns = [
    path('<int: cid>', views.college, name='college'),
    path('', views.collegesList, name='collegesList'),

]
