from django.shortcuts import render

# Create your views here.
def addTeacher(request) :
  return render(request, 'addTeacher/addTeacher.html')