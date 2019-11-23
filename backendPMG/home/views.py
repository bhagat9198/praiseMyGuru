from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Try

# Create your views here.
def home(request):
  if request.method == 'POST':
    # uplaodedFile = request.FILES['img']
    # fs = FileSystemStorage()
    # imgname = fs.save(uplaodedFile.name, uplaodedFile)
    # url = fs.url(imgname)  
    # print(uplaodedFile.name)
    # print(uplaodedFile.size)

    n = request.POST['name']
    t = request.POST['range']
    # r = request.POST['expirance']
    # l = request.POST['subjects']
    # d = request.POST['institudename']
    # n = request.POST['num']
    info = Try(name = n, txt = t)
    info.save()
    return redirect('signin')
  else :
    return render(request, 'home/home.html')