from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
  if request.method == 'post':
    uplaodedFile = request.FILES('doc')
    print(uplaodedFile.name)
    print(uplaodedFile.size)
    fs = FileSystemStorage()
    fs.save(uplaodedFile.name, uplaodedFile)
  else:
    return render(request, 'home/home.html')