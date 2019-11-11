from django.shortcuts import render

# Create your views here.
def teachersList(request):
  return render(request, 'teachers/teachersList.html')

def praiseTeacher(request):
  return render(request, 'teachers/praiseTeacher.html')

def teacher(request, id):
  return render(request, 'teachers/teacher.html')