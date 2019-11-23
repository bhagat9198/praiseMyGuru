from django.shortcuts import render, get_object_or_404
from add.models import AddTeacher
# Create your views here.

def gurusList(request):
  gurusList = AddTeacher.objects.all()

  context = {
    'gurusList' : gurusList
  }
  
  return render(request,'gurus/gurusList.html', context)

def praiseGuru(request):
  return render(request,'gurus/praiseGuru.html')

def guru(request):
  return render(request,'gurus/guru.html')