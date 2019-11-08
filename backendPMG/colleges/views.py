from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def collegesList(request) :
  return render(request,'colleges/collegesList.html')
