from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import timezone
from .models import Feedback
from django.contrib import messages

# Create your views here.


def aboutus(request):

  if request.method == 'POST' :
    # counter = counter + 1
    # id = counter
    name = request.POST['name']
    email = request.POST['email']
    exp = request.POST['expirence']
    helpp = request.POST['help']
    category = request.POST['category']
    suggestion = request.POST['suggestion']
    dateTime = timezone.now()
    feedback = Feedback(name = name, email = email, exp = exp, helpp = helpp, category = category, suggestion = suggestion, dateTime = dateTime)
    feedback.save()
    messages.add_message(request, messages.SUCCESS, 'You got your suggestion. It means a lot to us!!')
    return render(request, 'aboutus/aboutus.html')
  else:
    return render(request, 'aboutus/aboutus.html')

# counter = 0