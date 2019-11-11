from django.shortcuts import render

# Create your views here.
def collegesList(request) :
  return render(request, 'colleges/collegesList.html')

def college(request, id) :
  return render(request, 'colleges/college.html')