from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    # return HttpResponse("wELCOME hOME")
    context={
        "var":"this is a variable"
    } 
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def services(request):
    return HttpResponse("Servicessss")
def contact(request):
    if request.method=='POST':
        email=request.POST.get('inputEmail')
        address=request.POST.get('inputAddress')
        phno=request.POST.get('inputPhno')
        desc=request.POST.get('inputDetails')
        obj=Contact(email=email,address=address,phno=phno,desc=desc,date=datetime.today())
        obj.save()

    return render(request,"contact.html")