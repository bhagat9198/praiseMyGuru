from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.guru, name='guru'),
    path('praise/<int:parise_id>',views.praiseGuru, name='praiseGuru'),
    path('',views.gurusList, name='gurusList'),
]