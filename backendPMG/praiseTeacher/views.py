from django.shortcuts import render

# Create your views here.
def praiseTeacher(request) :
  return render(request, 'praiseTeacher/praiseTeacher.html')