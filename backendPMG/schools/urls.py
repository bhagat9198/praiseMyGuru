from django.urls import path
from . import views

urlpatterns = [
  path('signin',views.schoolsList, name='schoolsList'),
]