from django.shortcuts import render,redirect

# Create your views here.

def index(req):
    return render(req,'index.html')
def login(req):
    if req.method=='POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        
    return render(req,'login.html')
def logout(req):
    return render(req,'login.html')