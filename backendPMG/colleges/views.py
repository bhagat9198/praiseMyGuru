from django.shortcuts import render, get_list_or_404
from add.models import AddCollege

# Create your views here.
def collegesList(request) :
  collegeList = AddCollege.objects.all()

  context = {
    'collegeList' : collegeList
  }

  return render(request,'colleges/collegesList.html',context)

def college(request, cid) :
  collegeDetail = get_list_or_404(AddCollege, pk = cid)

  context = {
    'collegeDetail' : collegeDetail
  }
  return render(request,'colleges/college.html',context)