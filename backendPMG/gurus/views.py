from django.shortcuts import render

# Create your views here.

def gurusList(request):
  return render(request,'gurus/gurusList.html')

def praiseGuru(request):
  return render(request,'gurus/praiseGuru.html')

def guru(request):
  return render(request,'gurus/guru.html')