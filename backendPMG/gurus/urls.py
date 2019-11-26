from django.urls import path
from . import views

urlpatterns = [
    path('praise/<int:parise_id>',views.praiseGuru, name='praiseGuru'),
    path('<int:guru_id>', views.guru, name='guru'),
    path('',views.gurusList, name='gurusList'),
]