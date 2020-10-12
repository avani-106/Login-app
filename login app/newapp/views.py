from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import details

# Create your views here
def signup(request):
    if request.session.has_key('email_session') & request.session.has_key('password_session'):
        return render(request,"home.html") 
    else:  
         return render(request,"signup.html")
     
     
def home(request):
    if request.session.has_key('email_session') & request.session.has_key('password_session'):
        return render(request,"home.html") 
    else:  
        return render(request,"login.html")
     
    

def add(request):
    obj=details()
    obj.name=request.POST['name']
    obj.email=request.POST['email']
    obj.password=request.POST['password']
    obj.save()
    request.session['email_session']=obj.email
    request.session['password_session']=obj.password
    return render(request,"home.html")

def login(request):
    if request.session.has_key('email_session') & request.session.has_key('password_session'):
        return render(request,"home.html") 
    else:
        if request.COOKIES.get('email_cookie'):
            em_cookie=request.COOKIES('email_cookie')
            pass_cookie=request.COOKIES('password_cookie')
            return render(request,'login.html',{'email_cookie':em_cookie,'password_cookie':pass_cookie})
        else:
            return render(request,"login.html")   

def verify(request):
    em=request.POST['email']
    pas=request.POST['password']
    cb=request.POST.get('cb',False)
    res=details.objects.filter(email=em).filter(password=pas)
    if (res):
        response=render(request,"home.html")
        request.session['email_session']=em
        request.session['password_session']=pas
        if cb:
            response.set_cookie('email_cookie',em,2*60)
            response.set_cookie('password_cookie',pas,2*60)
            return response
        else:
            return render(request,"home.html")
    else:
        return render(request,"login.html")            
        
        
def logout(request):
    if request.method=='POST':
        del request.session['email_session']
        del request.session['password_session']
        return render(request,"login.html")
        response.delete_cookie('email_cookie')
        response.delete_cookie('password_cookie')
        return response 
    
    
    
    
    
    
        
    
    
    