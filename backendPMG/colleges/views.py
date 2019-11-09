from django.shortcuts import render

# Create your views here.
def collegesList(request) :
  return render(request, 'colleges/collegesList.html')
