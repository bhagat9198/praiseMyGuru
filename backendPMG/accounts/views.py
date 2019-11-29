from django.shortcuts import render, redirect
from .models import Signups, Dashbord
from datetime import datetime
from django.utils import timezone
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.
def signout(request) :
  if request.method == 'POST' :
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'You are logged out !')
    return render(request, 'home/home.html')

def signin(request) :
  if request.method == 'POST':
    uname = request.POST['username']
    pass1 = request.POST['password']

    user = auth.authenticate(username = uname, password = pass1 )
    if user is not None:
      auth.login(request, user)
      messages.add_message(request, messages.SUCCESS, 'You are logged in!')
      return redirect('dashbord')
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

@login_required(login_url='signin')
def dashbord(request) :
  if request.method == 'POST' :
    current_userID = Signups.objects.get(pk = 1)
    status = request.POST['onmind']
    uplaodedFile = request.FILES['imgupload']
    fs = FileSystemStorage()
    imgname = fs.save(uplaodedFile.name, uplaodedFile)
    url = fs.url(imgname)
    dateTime = timezone.now();

    userdashbord = Dashbord(userID = current_userID, status = status, image = url, dateTime = dateTime)
    userdashbord.save();
    return redirect('dashbord')
  else :
    
    return render(request, 'accounts/dashbord.html')
  
