from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def schoolsList(request) :
  return render(request,'schools/schoolsList.html')
