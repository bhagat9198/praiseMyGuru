from django.shortcuts import render
from add.models import AddSchool

# Create your views here.
def schoolsList(request) :
  schoolList = AddSchool.objects.all()

  context = {
    'schoolList' : schoolList
  }

  return render(request,'schools/schoolsList.html', context)

def school(request, id) :
  return render(request,'schools/school.html')
