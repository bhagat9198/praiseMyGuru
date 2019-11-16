from django.shortcuts import render, redirect
from .models import Signups
from datetime import datetime
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from  django.contrib import auth

# Create your views here.
def signin(request) :
  if request.method == 'POST':
    uname = request.POST['username']
    pass1 = request.POST['password']

    user = auth.authenticate(username = uname, password = pass1 )
    if user is not None:
      auth.login(request, user)
      messages.add_message(request, messages.SUCCESS, 'You are logged in!')
      return redirect('home')
    else :
      messages.add_message(request, messages.INFO, 'Username or password incorrect')
      return redirect('signin')
  else:
    return render(request, 'accounts/signin.html')


def signup(request) :
  if request.method == 'POST':
    #get the form values
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['password1']
    category = request.POST['category']
    term = request.POST['terms']
    if term == 'on':
      term = True
    else:
      term = False

    if password == cpassword :
      if Signups.objects.filter(userName = uname).exists() :
        messages.add_message(request, messages.INFO, 'Username alraedy exits')
        return redirect('signup')
      else:
        if Signups.objects.filter(email = email).exists() :
          messages.add_message(request, messages.INFO, 'Email alraedy exits')
          return redirect('signup')
        else:
          userInfo = Signups(firstName = fname, lastName = lname, userName = uname, email = email, password = password, confirmPassword = cpassword, category = category, agreeTerms = term, dateTime = datetime.now())
          userInfo.save()
          user = User.objects.create_user(username = uname, password = password, first_name = fname, last_name = lname, email = email)
          return redirect('signin')
    else :
      messages.add_message(request, messages.INFO, 'Password didnt match')
      return redirect('signup')

  else :
    return render(request, 'accounts/signup.html')


  
