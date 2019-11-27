from django.shortcuts import render, get_object_or_404
from add.models import AddTeacher
from datetime import datetime
from django.utils import timezone
from .models import Praise
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from accounts.models import Signups

# Create your views here.

def gurusList(request):
  gurusList = AddTeacher.objects.all()

  context = {
    'gurusList' : gurusList
  }
  
  return render(request,'gurus/gurusList.html', context)

@login_required(login_url='signin')
def praiseGuru(request,parise_id):
  gurus = get_object_or_404(AddTeacher, pk = parise_id)
  context = {
    'gurus' : gurus
  }

  if request.method == 'POST' :
    current_userID = Signups.objects.get(userName = request.user.username)
    addteacherID = parise_id
    worthListening = request.POST['worthlisten']
    starts = request.POST['star']
    subjects = request.POST.getlist('subjects')
    tags = request.POST.getlist('tags')
    suggest = request.POST['suggest']
    suggestion = request.POST['suggestions']
    datetime = timezone.now()
    praiseinfo = Praise(userID = current_userID, addteacherID = addteacherID, worthListening =worthListening, starts = starts, subjects = subjects, tags =tags, suggest = suggest, suggestion = suggestion, datetime = datetime)
    praiseinfo.save()
    return render(request,'home/home.html')
  else :
    return render(request,'gurus/praiseGuru.html', context)

  
def guru(request,pk):
  gurus = get_object_or_404(AddTeacher, pk = pk)
  context = {
    'gurus' : gurus
  }

  return render(request,'gurus/guru.html', context)

