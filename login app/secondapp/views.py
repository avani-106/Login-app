from django.shortcuts import render
from django.http import HttpResponse
from .models import employee
# Create your views here.
from django.core.files.storage import FileSystemStorage

def direct(request):
    return render(request,"imageform.html")

def upload(request):
    obj=employee()
    obj.name=request.POST['name']
    img=request.FILES['img']
    obj.image=img
    ext=["jpg","jpeg","png","svg"]
    if img.name.endswith(tuple(ext)):
        maxSize=2000000
        if img.size<maxSize:
            obj.save()
            fobj=FileSystemStorage() #
            fobj.save(img.name,img) #
            return HttpResponse("file uploaded")
        else:
            return HttpResponse("size greator than 2 MB")
    else:
        return HttpResponse("file is not an image")

