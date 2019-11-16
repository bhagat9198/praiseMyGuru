from django.shortcuts import render, redirect
from .models import AddTeacher

# Create your views here.
def addTeacher(request) :
  if request.method == 'POST' :
    fname = request.POST['firstname']
    lname = request.POST['lastname']
    institute_type = request.POST['Institutetype']
    institute_name = request.POST['institudename']
    subjects = request.POST.getlist['subjects']
    age = request.POST['age']
    expirance = request.POST['expirance']
    # imgupload = request.FILES['imguplaod']
    myfile = request.FILES['imguplaod']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    teachermoto = request.POST['teachermoto']

    addteacher = AddTeacher(firstName = fname, lastName = lname, instituteType = institute_type, institute = institute_name, subjects = subjects, age = age, expirence = expirance,  moto = teachermoto);
    addteacher.save()
    # return redirect('home')
    return render(request, 'addTeacher/addTeacher.html')

  else :
    return render(request, 'addTeacher/addTeacher.html')