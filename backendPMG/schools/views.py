from django.shortcuts import render

# Create your views here.
def schoolsList(request) :
  return render(request, 'schools/schoolsList.html')

def school(request, id) :
  return render(request, 'schools/school.html')
