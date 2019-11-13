from django.urls import path
from . import views

urlpatterns = [
    path('',views.gurusList, name='gurusList'),
    path('praise/',views.praiseGuru, name='praiseGuru'),
    path('guru/', views.guru, name='guru'),
]